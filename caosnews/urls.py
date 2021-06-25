from django.urls import path
from .views import (
    Home,
    noticia,
    Autor,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("noticia/<noticia_id>", noticia, name="noticia"),
    path("autor/<autor_id>", Autor.as_view(), name="autor")
]