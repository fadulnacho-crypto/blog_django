"""Rutas principales del proyecto blog_project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Las rutas del blog estan organizadas en posts/urls.py
    path("", include("posts.urls")),
]

# Servir las imagenes subidas (MEDIA) durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
