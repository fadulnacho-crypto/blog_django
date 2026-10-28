"""Views basadas en funciones de la app posts."""

from django.shortcuts import render

from .models import Post


def inicio(request):
    """Pagina de inicio: muestra los ultimos 3 posts publicados."""
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    context = {
        "posts": ultimos_posts,
    }
    return render(request, "posts/inicio.html", context)


def lista_posts(request):
    """Listado de todos los posts publicados, consultados con el ORM."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts,
    }
    return render(request, "posts/lista_posts.html", context)


def acerca(request):
    """Pagina 'Acerca de' con informacion del autor y del sitio."""
    return render(request, "posts/acerca.html")
