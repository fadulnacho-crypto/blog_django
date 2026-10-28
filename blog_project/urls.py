"""Rutas principales del proyecto blog_project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Las rutas del blog estan organizadas en posts/urls.py
    path("", include("posts.urls")),
]
