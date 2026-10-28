"""Views basadas en funciones de la app posts."""

from django.shortcuts import render

# Datos de ejemplo (todavia sin base de datos ni modelos)
POSTS_EJEMPLO = [
    {
        "titulo": "Introduccion a Python",
        "resumen": "Python es un lenguaje simple y poderoso para empezar a programar.",
        "tags": ["python", "programacion"],
    },
    {
        "titulo": "Primeros pasos con Django",
        "resumen": "Como pasar de un blog por consola a un sitio web real.",
        "tags": ["django", "web"],
    },
    {
        "titulo": "Consejos para aprender a programar",
        "resumen": "Practicar todos los dias es la clave.",
        "tags": ["consejos"],
    },
]


def inicio(request):
    """Pagina de inicio del blog."""
    return render(request, "posts/inicio.html")


def lista_posts(request):
    """Listado de posts de ejemplo."""
    return render(request, "posts/lista_posts.html", {"posts": POSTS_EJEMPLO})


def acerca(request):
    """Pagina 'Acerca de' con informacion del autor y del sitio."""
    return render(request, "posts/acerca.html")
