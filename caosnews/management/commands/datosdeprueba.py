from django.core.management.base import BaseCommand
from caosnews.models import Usuario, Colaborador, Publicacion
from caosnews.tipo_usuario import Tipo
from .generarusuarios import Command as GeneradorUsuarios
from .generarnoticias import Command as GeneradorNoticias


def crear_superusuario():
    print("generando un admin...")
    admin = Usuario(username="admin", email="admin@admin.com")
    admin.set_password("admin")
    admin.is_staff = True
    admin.is_superuser = True
    admin.is_active = True
    admin.tipo_usuario = Tipo.ADMINISTRADOR.value
    admin.save()


def eliminar_todo():
    Publicacion.objects.all().delete()
    Colaborador.objects.all().delete()
    Usuario.objects.all().delete()


class Command(BaseCommand):
    help = "Puebla la base de datos con data de prueba"

    def handle(self, *args, **options):
        eliminar_todo()
        crear_superusuario()
        GeneradorUsuarios().handle()
        GeneradorNoticias().handle()
