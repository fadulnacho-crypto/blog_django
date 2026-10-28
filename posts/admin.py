from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Configuracion del modelo Post en el panel /admin/."""

    list_display = ("titulo", "autor", "estado", "fecha_creacion")
    list_filter = ("estado", "fecha_creacion")
    search_fields = ("titulo", "contenido", "autor")
    list_editable = ("estado",)
