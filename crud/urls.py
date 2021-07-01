from django.urls import path
from .views import (crud_index,
                    ver_editores,
                    ver_noticias,
                    ver_colaboradores,
                    editar_noticias,
                    editar_editor,
                    editar_colaborador,
                    agregar_editor,
                    agregar_colaborador,
                    agregar_noticia,
                    borrar_noticia,
                    borrar_usuario)

urlpatterns = [
    path("", crud_index, name="crud_index"),
    path("editores", ver_editores, name='vista_editores'),
    path("nuevo/editor", agregar_editor, name="agregar_editor"),
    path("editor/<id_editor>", editar_editor, name="editar_editor"),

    path("colaboradores", ver_colaboradores, name="vista_colaboradores"),
    path("nuevo/colaborador", agregar_colaborador, name="agregar_colaborador"),
    path("colaborador/<id_colab>", editar_colaborador, name="editar_colab"),

    path("noticias", ver_noticias, name="vista_noticias"),
    path("nuevo/noticia", agregar_noticia, name="agregar_noticia"),
    path("noticia/<id_noticia>", editar_noticias, name="editar_noticia"),
    path("borrar/noticia/<id_noticia>", borrar_noticia, name="borrar_noticia"),

    path("borrar/usuario/<id_usuario>", borrar_usuario, name="borrar_usuario"),
]
