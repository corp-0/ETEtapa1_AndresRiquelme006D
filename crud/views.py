from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

# Create your views here.
from caosnews.models import Colaborador, Usuario, Publicacion
from caosnews.tipo_usuario import Tipo
from .forms import ColaboradorForm, NoticiaForm, CrearUsuarioForm, EditarUsuario


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
    finally:
        cuerpo_tabla = []
        for c in editores:
            d = {
                "campos": [c.pk, c.username],
                "url_editar": str(reverse('editar_editor', args=[c.pk]))[:-1],
                "url_eliminar": str(reverse('borrar_usuario', args=[c.pk]))[:-1]
            }
            cuerpo_tabla.append(d)

        contexto = {
            "title": "Lista Editores",
            "clases_editores": "active",
            "enlace_agregar": reverse('agregar_editor'),
            "headers_tabla": ["ID", "Nombre usuario"],
            "cuerpo_tabla": cuerpo_tabla,
            "paginado": editores
        }

    return render(request, 'CRUD/vista_tabla.html', contexto)


@login_required(login_url='/admin/login/')
def editar_editor(request, id_editor):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    editor = Usuario.objects.get(pk=id_editor)
    formulario = EditarUsuario(instance=editor)
    contexto = {
        "formulario_1": formulario,
        "title": "Editar editor"
    }

    if request.method == "POST":
        formulario = EditarUsuario(request.POST, instance=editor)
        if formulario.is_valid():
            formulario.instance.set_password(request.POST.get("id_password"))
            formulario.save()
            messages.success(request, f"¡Editor {editor} editado con éxito!")
        else:
            mostrar_errores(request, formulario.errors)
        return redirect('vista_editores')

    return render(request, 'CRUD/formulario.html', contexto)


@login_required(login_url='/admin/login/')
def agregar_editor(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    formulario = CrearUsuarioForm()
    contexto = {
        "title": "Crear Editor",
        "formulario_1": formulario,
    }

    if request.method == "POST":
        formulario = CrearUsuarioForm(request.POST)
        formulario.instance.tipo_usuario = Tipo.EDITOR.value

        if formulario.is_valid():
            formulario.save()
            messages.success(request, f"¡Editor {formulario.instance} creado con éxito!")
        else:
            mostrar_errores(request, formulario.errors)

        return redirect('vista_editores')

    return render(request, 'CRUD/formulario.html', contexto)


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
    finally:
        cuerpo_tabla = []
        for c in colaboradores:
            d = {
                "campos": [c.user, c.nombre, c.rut, c.fono, c.direccion, c.pais],
                "url_editar": str(reverse('editar_colab', args=[c.pk]))[:-1],
                "url_eliminar": str(reverse('borrar_usuario', args=[c.pk]))[:-1]
            }
            cuerpo_tabla.append(d)

        contexto = {
            "title": "Lista Colaboradores",
            "clases_colaboradores": "active",
            "enlace_agregar": reverse('agregar_colaborador'),
            "headers_tabla": ["Cuenta asociada", "Nombre completo", "RUT", "Fono", "Dirección", "País"],
            "cuerpo_tabla": cuerpo_tabla,
            "paginado": colaboradores
        }

    return render(request, 'CRUD/vista_tabla.html', contexto)


@login_required(login_url='/admin/login/')
def editar_colaborador(request, id_colab):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    usuario = Usuario.objects.get(pk=id_colab)
    colab = Colaborador.objects.get(user=usuario)

    formulario_1 = EditarUsuario(instance=usuario)
    formulario_2 = ColaboradorForm(instance=colab)

    contexto = {
        "formulario_1": formulario_1,
        "formulario_2": formulario_2,
        "title": "Editar editor"
    }

    if request.method == "POST":
        formulario_1 = EditarUsuario(request.POST, instance=usuario)
        formulario_2 = ColaboradorForm(request.POST, instance=colab)
        if formulario_1.is_valid() and formulario_2.is_valid():

            formulario_1.instance.set_password(request.POST.get("id_password"))
            formulario_1.save()
            formulario_2.save()

            messages.success(request, f"¡Colaborador {colab} editado con éxito!")
        else:
            mostrar_errores(request, formulario_1.errors)
            mostrar_errores(request, formulario_2.errors)
        return redirect('vista_colaboradores')

    return render(request, 'CRUD/formulario.html', contexto)


@login_required(login_url='/admin/login/')
def agregar_colaborador(request):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    usuario_form = CrearUsuarioForm()
    colab_form = ColaboradorForm()

    contexto = {
        "title": "Nuevo colaborador",
        "formulario_1": usuario_form,
        "formulario_2": colab_form
    }

    if request.method == "POST":
        usuario_form = CrearUsuarioForm(request.POST)
        colab_form = ColaboradorForm(request.POST, request.FILES)

        usuario = usuario_form.instance
        usuario.tipo_usuario = Tipo.COLABORADOR.value
        usuario.set_unusable_password()

        if usuario_form.is_valid() and colab_form.is_valid():
            usuario = usuario_form.save()

            colab = colab_form.instance
            colab.user = usuario

            colab = colab_form.save()
            pswd = colab.generar_pass_temporal()
            print(pswd)
            usuario.set_password(pswd)
            usuario.save()

            messages.success(request, f"¡Colaborador {colab.nombre} creado con éxito!")
        else:
            mostrar_errores(request, usuario_form.errors)
            mostrar_errores(request, colab_form.errors)

        return redirect('vista_colaboradores')


    return render(request, 'CRUD/formulario.html', contexto)


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
    finally:
        cuerpo_tabla = []
        for c in noticias:
            d = {
                "campos": [c.autor,
                           c.fecha,
                           c.titulo,
                           '<i class="material-icons green-text">toggle_on</i>' if c.publicada else '<i class="material-icons gray-text">toggle_off</i>'],
                "url_editar": str(reverse('editar_noticia', args=[c.pk]))[:-1],
                "url_eliminar": str(reverse('borrar_noticia', args=[c.pk]))[:-1]
            }
            cuerpo_tabla.append(d)

        contexto = {
            "title": "Lista Noticias",
            "clases_noticias": "active",
            "enlace_agregar": reverse('agregar_noticia'),
            "headers_tabla": ["Autor", "Fecha publicación", "Título", "Publicada"],
            "cuerpo_tabla": cuerpo_tabla,
            "paginado": noticias
        }

    return render(request, 'CRUD/vista_tabla.html', contexto)


@login_required(login_url='/admin/login/')
def editar_noticias(request, id_noticia):
    if not request.user.es_almenos_editor():
        return HttpResponse(status=403)

    noticia = Publicacion.objects.get(pk=id_noticia)
    formulario = NoticiaForm(instance=noticia)
    contexto = {
        "formulario_1": formulario,
        "title": "Editar noticia"
    }

    if request.method == "POST":
        formulario = NoticiaForm(request.POST, instance=noticia)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f"¡Noticia {noticia} editada con éxito!")
        else:
            mostrar_errores(request, formulario.errors)
        return redirect('vista_noticias')

    return render(request, 'CRUD/formulario.html', contexto)


@login_required(login_url='/admin/login/')
def agregar_noticia(request):
    if not request.user.es_almenos_editor():
        return HttpResponse(status=403)

    noticia_form = NoticiaForm

    contexto = {
        "formulario_1": noticia_form
    }

    if request.method == "POST":
        noticia_form = NoticiaForm(request.POST)
        if noticia_form.is_valid():
            messages.success(request, f"¡Noticia {noticia_form.instance.titulo} fue creada!")
            noticia_form.save()
        else:
            mostrar_errores(request, noticia_form.errors)

        return  redirect('vista_noticias')

    return render(request, 'CRUD/formulario.html', contexto)


@login_required(login_url='/admin/login/')
def borrar_noticia(request, id_noticia):
    if not request.user.es_almenos_editor():
        return HttpResponse(status=403)

    return eliminar_modelo(Publicacion, id_noticia, request, "Noticia")


@login_required(login_url='/admin/login/')
def borrar_usuario(request, id_usuario):
    if not request.user.es_sysadmin():
        return HttpResponse(status=403)

    return eliminar_modelo(Usuario, id_usuario, request, "Usuario")


def eliminar_modelo(modelo, pk, request, texto):
    entrada = modelo.objects.get(pk=pk)
    entrada.delete()

    messages.success(request, f"¡{texto}: {entrada} fue eliminado!")
    referer = request.META.get("HTTP_REFERER")

    return HttpResponseRedirect(referer)


def mostrar_errores(request, errores):
    for k, v in errores.items():
        messages.error(request, f"Campo {k}: {v}")
