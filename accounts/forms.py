"""Formularios de usuarios: registro, datos del usuario y perfil."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil


class RegistroForm(UserCreationForm):
    """Formulario de registro basado en UserCreationForm, con email y nombre."""

    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="Nombre", max_length=150, required=False)
    last_name = forms.CharField(label="Apellido", max_length=150, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese email.")
        return email


class UsuarioForm(forms.ModelForm):
    """Datos basicos del usuario que se pueden editar desde el perfil."""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        labels = {"first_name": "Nombre", "last_name": "Apellido", "email": "Email"}


class PerfilForm(forms.ModelForm):
    """Biografia, sitio web y avatar del perfil."""

    class Meta:
        model = Perfil
        fields = ("biografia", "link_web", "avatar")
        labels = {
            "biografia": "Biografía",
            "link_web": "Sitio web (opcional)",
            "avatar": "Avatar (opcional)",
        }
        widgets = {
            "biografia": forms.Textarea(attrs={"rows": 5, "placeholder": "Contá algo sobre vos..."}),
            "link_web": forms.URLInput(attrs={"placeholder": "https://..."}),
        }
