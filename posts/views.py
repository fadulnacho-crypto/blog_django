"""Views basadas en funciones de la app posts (incluye el CRUD de Post)."""

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post

# Filtros disponibles en el listado: valor de ?estado= -> texto del boton
FILTROS_ESTADO = {
    "publicado": "Publicados",
    "borrador": "Borradores",
    "archivado": "Archivados",
    "todos": "Todos",
}


def inicio(request):
    """Pagina de inicio: muestra los ultimos 3 posts publicados."""
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    return render(request, "posts/inicio.html", {"posts": ultimos_posts})


def acerca(request):
    """Pagina 'Acerca de' con informacion del autor y del sitio."""
    return render(request, "posts/acerca.html")


# ----- CRUD -----

def lista_posts(request):
    """READ (listado): por defecto muestra los publicados; ?estado= cambia el filtro."""
    estado = request.GET.get("estado", "publicado")
    if estado not in FILTROS_ESTADO:
        estado = "publicado"

    posts = Post.objects.all().order_by("-fecha_creacion")
    if estado != "todos":
        posts = posts.filter(estado=estado)

    context = {
        "posts": posts,
        "estado_actual": estado,
        "filtros": FILTROS_ESTADO,
    }
    return render(request, "posts/lista_posts.html", context)


def detalle_post(request, pk):
    """READ (detalle): muestra un post con su imagen, si tiene."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


def crear_post(request):
    """CREATE: muestra el formulario y guarda el nuevo post con su imagen."""
    if request.method == "POST":
        # request.FILES trae la imagen enviada por el formulario
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, "El post se creó correctamente.")
            return redirect("posts:detalle_post", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "posts/post_form.html", {"form": form, "accion": "Crear"})


def editar_post(request, pk):
    """UPDATE: edita un post existente y permite cambiar o quitar la imagen."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "El post se actualizó correctamente.")
            return redirect("posts:detalle_post", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/post_form.html", {"form": form, "accion": "Editar", "post": post})


def eliminar_post(request, pk):
    """DELETE: pide confirmacion (GET) y elimina el post (POST)."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        titulo = post.titulo
        if post.imagen:
            post.imagen.delete(save=False)  # borra tambien el archivo de la imagen
        post.delete()
        messages.success(request, f'El post "{titulo}" se eliminó.')
        return redirect("posts:lista_posts")
    return render(request, "posts/post_confirm_delete.html", {"post": post})
