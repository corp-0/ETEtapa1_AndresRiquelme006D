import urllib.parse

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

# Create your views here.
from caosnews.models import Colaborador, Usuario, Publicacion
from caosnews.tipo_usuario import Tipo


@login_required(login_url='/admin/login/')
def crud_index(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    return render(request, 'CRUD/index.html', {"title": "Índice"})


@login_required(login_url='/admin/login/')
def ver_editores(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    editores = Usuario.objects.filter(tipo_usuario=Tipo.EDITOR.value).order_by("date_joined")
    page = request.GET.get("page", 1)
    paginator = Paginator(editores, 5)

    try:
        editores = paginator.page(page)
    except PageNotAnInteger:
        editores = paginator.page(1)
    except EmptyPage:
        editores = paginator.page(paginator.num_pages)

    return render(request, 'CRUD/editores.html', {"title": "Editores", "editores": editores})


@login_required(login_url='/admin/login/')
def editar_editor(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    return HttpResponse("editar_editor")


@login_required(login_url='/admin/login/')
def agregar_editor(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    return HttpResponse("agregar_editor")


@login_required(login_url='/admin/login/')
def ver_colaboradores(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    colaboradores = Colaborador.objects.all().order_by("user__date_joined")
    page = request.GET.get("page", 1)
    paginator = Paginator(colaboradores, 5)

    try:
        colaboradores = paginator.page(page)
    except PageNotAnInteger:
        colaboradores = paginator.page(1)
    except EmptyPage:
        colaboradores = paginator.page(paginator.num_pages)

    return render(request, 'CRUD/colaboradores.html', {"title": "Colaboradores", "colaboradores": colaboradores})


@login_required(login_url='/admin/login/')
def editar_colaborador(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    return HttpResponse("editar_colaborador")


@login_required(login_url='/admin/login/')
def agregar_colaborador(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    return HttpResponse("agregar_colaborador")


@login_required(login_url='/admin/login/')
def ver_noticias(request):
    if not request.user.es_almenos_editor():
        return HttpResponse(status=403)

    noticias = Publicacion.objects.all().order_by("-fecha")
    page = request.GET.get("page", 1)
    paginator = Paginator(noticias, 5)

    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        noticias = paginator.page(1)
    except EmptyPage:
        noticias = paginator.page(paginator.num_pages)

    return render(request, 'CRUD/noticias.html', {"title": "Noticias", "noticias": noticias})


@login_required(login_url='/admin/login/')
def editar_noticias(request):
    return HttpResponse("editar_noticia")


@login_required(login_url='/admin/login/')
def agregar_noticia(request):
    if not request.user.es_almenos_editor():
        return HttpResponse(status=403)

    return HttpResponse("agregar_noticia")


@login_required(login_url='/admin/login/')
def borrar_noticia(request, id_noticia):
    if not request.user.es_almenos_editor():
        return HttpResponse(status=403)

    return eliminar_modelo(Publicacion, id_noticia, request)


@login_required(login_url='/admin/login/')
def borrar_usuario(request, id_usuario):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    return eliminar_modelo(Usuario, id_usuario, request)


def eliminar_modelo(modelo, pk, request):
    entrada = modelo.objects.get(pk=pk)
    entrada.delete()

    contexto = {"mensaje": f"Operación realizada exitosamente"}
    referer = request.META.get("HTTP_REFERER")
    param_pos = referer.find("?")
    if param_pos > 0:
        referer = referer[:param_pos]

    return HttpResponseRedirect(
        referer + '?' + urllib.parse.urlencode(contexto))

