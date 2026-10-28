"""Views de usuarios: registro, perfil y edicion de perfil.

Login, logout y cambio de contrasena usan las vistas nativas de Django
(configuradas en accounts/urls.py).
"""

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PerfilForm, RegistroForm, UsuarioForm
from .models import Perfil


def registro(request):
    """Crea un usuario nuevo, le crea su Perfil e inicia la sesion."""
    if request.user.is_authenticated:
        return redirect("perfil")

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # El perfil se crea explicitamente despues de guardar el usuario
            Perfil.objects.create(user=usuario)
            login(request, usuario)
            messages.success(request, f"¡Bienvenido, {usuario.username}! Tu cuenta se creó correctamente.")
            return redirect("perfil")
    else:
        form = RegistroForm()
    return render(request, "accounts/registro.html", {"form": form})


@login_required
def perfil(request):
    """Muestra el perfil del usuario que inicio sesion."""
    # get_or_create cubre usuarios creados antes (por ejemplo con createsuperuser)
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {"perfil": perfil_usuario})


@login_required
def editar_perfil(request):
    """Edita los datos del usuario y su perfil (biografia, sitio web y avatar)."""
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST, instance=request.user)
        # request.FILES trae el avatar enviado por el formulario
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            messages.success(request, "Tu perfil se actualizó correctamente.")
            return redirect("perfil")
    else:
        usuario_form = UsuarioForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil_usuario)

    context = {
        "usuario_form": usuario_form,
        "perfil_form": perfil_form,
        "perfil": perfil_usuario,
    }
    return render(request, "accounts/editar_perfil.html", context)
