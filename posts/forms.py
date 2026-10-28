"""Formularios de la app posts."""

from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Formulario basado en el modelo Post para crear y editar publicaciones."""

    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "estado", "imagen"]
        labels = {
            "titulo": "Título",
            "contenido": "Contenido",
            "autor": "Autor",
            "estado": "Estado",
            "imagen": "Imagen (opcional)",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Título del post"}),
            "contenido": forms.Textarea(attrs={"rows": 8, "placeholder": "Escribí el contenido..."}),
            "autor": forms.TextInput(attrs={"placeholder": "Tu nombre"}),
        }
