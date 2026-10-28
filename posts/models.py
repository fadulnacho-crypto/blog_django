from django.db import models


class Post(models.Model):
    """Representa una publicacion del blog."""

    class Estado(models.TextChoices):
        BORRADOR = "borrador", "Borrador"
        PUBLICADO = "publicado", "Publicado"
        ARCHIVADO = "archivado", "Archivado"

    titulo = models.CharField("título", max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField("fecha de creación", auto_now_add=True)
    estado = models.CharField(
        max_length=10,
        choices=Estado.choices,
        default=Estado.BORRADOR,
    )

    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.titulo
