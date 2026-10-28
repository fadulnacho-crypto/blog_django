from django.contrib import admin

from .models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    """Perfiles de usuario en el panel /admin/."""

    list_display = ("user", "link_web", "tiene_avatar")
    search_fields = ("user__username", "user__email", "biografia")

    @admin.display(boolean=True, description="avatar")
    def tiene_avatar(self, obj):
        return bool(obj.avatar)
