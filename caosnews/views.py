from django.db.models import Max
from django.views.generic import ListView
from urllib import request
from django.utils.functional import cached_property
import os
from .models import Publicacion
import json

from functools import lru_cache


@lru_cache(maxsize=32)
def obtener_clima() -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Santiago&units=metric&lang=es&appid={os.getenv('CLIMA_API')}"
    r = request.urlopen(url)
    respuesta = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    print(respuesta)

    data = {
        "desc": respuesta["weather"][0]["description"],
        "icono": respuesta["weather"][0]["icon"],
        "temp": respuesta["main"]["temp"]
    }

    return data


class Home(ListView):
    template_name = "sitio/home.html"
    context_object_name = "posts"
    paginate_by = 4
    ordering = "-fecha"
    queryset = Publicacion.objects.filter(publicada=True)
    mas_visitas = Publicacion.objects.aggregate(Max("visitas"))
    noticia_caliente = Publicacion.objects.filter(visitas=mas_visitas["visitas__max"]).first()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context["title"] = "Home"
        context["noticia_caliente"] = self.noticia_caliente
        context["el_clima"] = obtener_clima()

        return context
