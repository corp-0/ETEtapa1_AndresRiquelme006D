from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, post_delete

from .model_mixins import ModelCacheMixin
from .listeners import clear_model_cache

from .usuario import TIPO_CHOICES, Tipo


class Usuario(AbstractUser):
    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPO_CHOICES)

    def __str__(self):
        return f"{Tipo(self.tipo_usuario).name} {self.username}"


class Colaborador(models.Model):
    user = models.OneToOneField(Usuario, verbose_name="Cuenta asociada", on_delete=models.CASCADE, primary_key=True)
    rut = models.CharField(max_length=12, verbose_name="RUN")
    foto = models.ImageField(verbose_name="Fotografía")
    nombre = models.CharField(max_length=200, verbose_name="Nombre completo")
    fono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    pais = models.CharField(max_length=15, verbose_name="País")

    def generar_pass_temporal(self) -> str:
        ident = f"{self.user.id.zfill(2)[:2]}"
        nombre = f"{self.nombre.upper()[:2]}"
        pais = f"{self.pais.lower()[-2:]}"
        fono = f"{self.fono[-2:]}"

        return f"{ident}{nombre}{pais}{fono}"

    def __str__(self):
        return f"{self.nombre}"


class Publicacion(models.Model, ModelCacheMixin):
    autor = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    fecha = models.DateTimeField(verbose_name="Fecha publicación", auto_now=True)
    titulo = models.CharField(max_length=250, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    publicada = models.BooleanField(verbose_name="Publicada", default=False)

    CACHE_KEY = "fecha"
    CACHED_RELATED_OBJECT = ["autor"]

    def __str__(self):
        return f"{self.titulo} por: {self.autor.nombre}"


post_save.connect(clear_model_cache, sender=Publicacion)
post_delete.connect(clear_model_cache, sender=Publicacion)
