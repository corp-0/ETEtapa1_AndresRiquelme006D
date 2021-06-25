from django.contrib import admin
from .models import Usuario, Colaborador, Publicacion


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("pk", "tipo_usuario", "username")
    ordering = ("pk",)

    fieldsets = (
        (
            "Datos usuario",
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password", 'tipo_usuario'),
            },
        ),
    )

    list_editable = ("tipo_usuario",)


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ("user", "nombre", "rut", "direccion", "fono", "pais")
    ordering = ("pk",)

    fieldsets = (
        (
            "Datos usuario",
            {
                "classes": ("wide",),
                "fields": ("user", "nombre", "rut", 'direccion', 'fono', 'pais', 'foto'),
            },
        ),
    )


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("pk", "autor", "fecha", "titulo", "publicada", "visitas")
    ordering = ("pk",)

