from django.contrib.auth.models import AbstractUser
from django.db import models
from .tipo_usuario import TIPO_CHOICES, Tipo


class Usuario(AbstractUser):
    """
    Objeto que representa una cuenta básica de usuario. Todos los tipos de usuarios que maneja el sitio
    usan esta cuenta como autentificación.
    """

    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPO_CHOICES, default=Tipo.COLABORADOR.value)

    def __str__(self):
        return f"{self.username}"

    def es_colaborador(self) -> bool:
        return self.tipo_usuario == Tipo.COLABORADOR.value

    def es_editor(self) -> bool:
        return self.tipo_usuario == Tipo.EDITOR.value

    def es_sysadmin(self) -> bool:
        return self.tipo_usuario == Tipo.ADMINISTRADOR.value

    def es_almenos_editor(self) -> bool:
        return self.tipo_usuario <= Tipo.EDITOR.value


class Colaborador(models.Model):
    """
    Objeto que representa a un usuario con cateogría de Colaborador.
    Los colaboradores no pueden registrarse, los crea el sysadmin y les otorga contraseñas temporales.

    Los colaboradores pueden crear noticias que serán luego aprobadas y publicadas por un editor.
    """
    user = models.OneToOneField(Usuario, verbose_name="Cuenta asociada", on_delete=models.CASCADE, primary_key=True,
                                db_index=True)
    rut = models.CharField(max_length=12, verbose_name="RUN")
    foto = models.ImageField(verbose_name="Fotografía", upload_to="subidas/img/")
    nombre = models.CharField(max_length=200, verbose_name="Nombre completo", db_index=True)
    fono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    pais = models.CharField(max_length=15, verbose_name="País")

    def generar_pass_temporal(self) -> str:
        ident = f"{str(self.user.id).zfill(2)[:2]}"
        nombre = f"{self.nombre.upper()[:2]}"
        pais = f"{self.pais.lower()[-2:]}"
        fono = f"{self.fono[-2:]}"

        return f"{ident}{nombre}{pais}{fono}"

    def __str__(self):
        return f"{self.nombre}"


class Publicacion(models.Model):
    """Representación de una noticia/publicación de blog en el sitio"""

    autor = models.ForeignKey(Colaborador, on_delete=models.CASCADE, db_index=True)
    fecha = models.DateTimeField(verbose_name="Fecha publicación", auto_now=True, db_index=True)
    titulo = models.CharField(max_length=250, verbose_name="Título", db_index=True)
    contenido = models.TextField(verbose_name="Contenido")
    publicada = models.BooleanField(verbose_name="Publicada", default=False)
    visitas = models.IntegerField(verbose_name="número de visitas", editable=False, default=0)

    def __str__(self):
        return f"{self.titulo} por: {self.autor.nombre}"
