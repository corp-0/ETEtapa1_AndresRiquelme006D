import random

from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

from .models import Publicacion

sin_noticias = {
    "titulo": "No hay noticias hoy!"
}


def home(request):
    posts = Publicacion.filter_from_cache(publicada=True)
    try:
        paginator = Paginator(posts, 2)
        numero_pagina = request.GET.get("page")
        noticias = paginator.get_page(numero_pagina)
    except EmptyPage:
        # noticia_caliente = sin_noticias
        noticias = [sin_noticias]
    # else:
    #     noticia_caliente = posts[random.randrange(0, len(posts))]

    contexto = {
        # "noticia_caliente": noticia_caliente,
        "posts": noticias,
        "title": "Home"
    }

    return render(request, 'sitio/home.html', contexto)
