from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    """Informacion extra de cada usuario. Relacion uno a uno con User."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil",
        verbose_name="usuario",
    )
    biografia = models.TextField("biografía", blank=True)
    link_web = models.URLField("sitio web", blank=True)
    avatar = models.ImageField(upload_to="avatares/", null=True, blank=True)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"

    def __str__(self):
        return f"Perfil de {self.user.username}"
