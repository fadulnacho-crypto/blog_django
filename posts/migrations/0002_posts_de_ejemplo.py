# Migracion de datos: carga posts de ejemplo para que el listado
# no quede vacio al clonar el repositorio y ejecutar "migrate".
# (db.sqlite3 no se sube a GitHub porque esta en .gitignore)

from django.db import migrations

POSTS_EJEMPLO = [
    {
        "titulo": "Introducción a Python",
        "contenido": "Python es un lenguaje simple y poderoso. Es ideal para empezar a programar "
                     "porque su sintaxis es clara y tiene una comunidad enorme.",
        "autor": "Ignacio Garcia Fadul",
        "estado": "publicado",
    },
    {
        "titulo": "Del blog por consola a Django",
        "contenido": "El blog empezó como un menú por consola con listas y diccionarios. "
                     "Después pasó a clases y JSON, y ahora es un sitio web con Django.",
        "autor": "Ignacio Garcia Fadul",
        "estado": "publicado",
    },
    {
        "titulo": "Consejos para aprender a programar",
        "contenido": "Practicar todos los días, armar proyectos propios y no tenerle miedo a los "
                     "errores: cada error es una pista de lo que hay que aprender.",
        "autor": "Ignacio Garcia Fadul",
        "estado": "publicado",
    },
    {
        "titulo": "Modelos y ORM en Django (borrador)",
        "contenido": "Este post todavía está en borrador, por eso no aparece en el sitio.",
        "autor": "Ignacio Garcia Fadul",
        "estado": "borrador",
    },
    {
        "titulo": "Instalando Python en Windows",
        "contenido": "Post archivado: ya no se muestra en el listado.",
        "autor": "Ignacio Garcia Fadul",
        "estado": "archivado",
    },
]


def crear_posts(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    for datos in POSTS_EJEMPLO:
        Post.objects.create(**datos)


def borrar_posts(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    titulos = [p["titulo"] for p in POSTS_EJEMPLO]
    Post.objects.filter(titulo__in=titulos).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(crear_posts, borrar_posts),
    ]
