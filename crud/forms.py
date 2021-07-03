from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from caosnews.models import Usuario, Colaborador, Publicacion


class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "password1", "password2")

class EditarUsuario(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ("username", "password")

class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        exclude = ("user", )

class NoticiaForm(ModelForm):
    class Meta:
        model = Publicacion
        exclude = ("fecha", "visitas")
