import json
import os
from functools import lru_cache
from urllib import request

from django.db.models import Max
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse

from .models import Publicacion, Colaborador


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


def noticia(request, noticia_id):
    pub = Publicacion.objects.get(pk=noticia_id)
    # TODO Horrible forma de contar visitas, no verifica si son únicas
    pub.visitas += 1
    pub.save()

    mas_noticias = Publicacion.objects.filter(publicada=True, autor=pub.autor_id).exclude(pk=pub.id)[:3]

    contexto = {
        "noticia": pub,
        "el_clima": obtener_clima(),
        "title": pub.titulo,
        "mas_noticias": mas_noticias
    }

    return render(request, 'sitio/noticia.html', contexto)


class Autor(ListView):
    template_name = "sitio/autor.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = "-fecha"

    def get_queryset(self):
        return Publicacion.objects.filter(publicada=True, autor=self.kwargs.get('autor_id', None))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Autor, self).get_context_data(**kwargs)
        autor = Colaborador.objects.get(user_id=self.kwargs.get("autor_id", None))
        noticias = Publicacion.objects.filter(autor=self.kwargs.get('autor_id', None))
        context["title"] = "Noticias de " + autor.nombre
        context["autor"] = autor
        context["total_noticias"] = noticias.count()
        context["noticias_publicadas"] = noticias.exclude(publicada=False).count()

        return context


