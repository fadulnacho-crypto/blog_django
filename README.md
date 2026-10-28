# Blog Django

Proyecto base de un blog web desarrollado con Django (Preentregas 7 a 10). Permite crear, ver, editar y eliminar posts con imagen desde el propio sitio.

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.
Incluye la configuración base del proyecto `blog_project` y una aplicación llamada `posts`.

Configuración aplicada en `blog_project/settings.py`:

- App `posts` registrada en `INSTALLED_APPS` como `posts.apps.PostsConfig`.
- Idioma: `LANGUAGE_CODE = "es-ar"`.
- Zona horaria: `TIME_ZONE = "America/Argentina/Buenos_Aires"`.

## Estructura

```
blog_django/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── media/
│   └── posts/          # imágenes subidas (no se suben a GitHub)
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── posts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── lista_posts.html
    │       ├── detalle_post.html
    │       ├── post_form.html
    │       ├── post_confirm_delete.html
    │       └── acerca.html
    └── static/
        └── posts/
            └── css/
                └── estilos.css
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/fadulnacho-crypto/blog_django.git
```

Entrar a la carpeta del proyecto:

```bash
cd blog_django
```

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual:

En Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Las dependencias son **Django** y **Pillow** (necesaria para el campo de imagen).

Crear la base de datos (aplica las migraciones y carga posts de ejemplo):

```bash
python manage.py migrate
```

## Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

Para detener el servidor: `Ctrl + C`.

## Aplicaciones

- **posts**: aplicación principal para manejar las publicaciones del blog.

## Páginas del sitio (Preentrega 8)

El sitio implementa el flujo completo de Django: **ruta → vista → template → archivos estáticos**.

| URL | View | Template |
|---|---|---|
| `/` | `inicio` | `posts/inicio.html` |
| `/posts/` | `lista_posts` | `posts/lista_posts.html` |
| `/acerca/` | `acerca` | `posts/acerca.html` |

- **Rutas:** definidas en `posts/urls.py` y conectadas al proyecto con `include()` en `blog_project/urls.py`.
- **Views:** funciones en `posts/views.py` que devuelven cada página con `render()`.
- **Templates:** en `posts/templates/posts/`. `base.html` tiene la estructura HTML5, `{% load static %}`, el menú de navegación y el bloque `{% block content %}`. Las demás páginas lo extienden con `{% extends 'posts/base.html' %}`.
- **Estáticos:** `posts/static/posts/css/estilos.css`, vinculado en `base.html` con `{% static 'posts/css/estilos.css' %}`.

## Modelo Post y base de datos (Preentrega 9)

El modelo `Post` (en `posts/models.py`) tiene los campos:

| Campo | Tipo | Detalle |
|---|---|---|
| `titulo` | `CharField` | Título del post. |
| `contenido` | `TextField` | Texto del post. |
| `autor` | `CharField` | Nombre de quien lo escribe. |
| `fecha_creacion` | `DateTimeField` | Se completa sola con `auto_now_add=True`. |
| `estado` | `CharField` con `choices` | `borrador`, `publicado` o `archivado`. |

El método `__str__` devuelve el título, así cada post se ve por su nombre en el admin.

- **Migraciones:** `0001_initial.py` crea la tabla del modelo. `0002_posts_de_ejemplo.py` carga 5 posts de ejemplo (3 publicados, 1 borrador y 1 archivado) para que el sitio no aparezca vacío al clonar el repo, ya que `db.sqlite3` no se sube a GitHub.
- **ORM:** las views `inicio` y `lista_posts` consultan `Post.objects.filter(estado="publicado").order_by("-fecha_creacion")` y envían los posts al template por contexto. Los templates los recorren con `{% for post in posts %}`. Solo se muestran los posts **publicados**.

## CRUD de posts con imágenes (Preentrega 10)

### Operaciones disponibles

| Operación | URL | View | Template |
|---|---|---|---|
| Listar (Read) | `/posts/` | `lista_posts` | `lista_posts.html` |
| Ver detalle (Read) | `/posts/<id>/` | `detalle_post` | `detalle_post.html` |
| Crear (Create) | `/posts/crear/` | `crear_post` | `post_form.html` |
| Editar (Update) | `/posts/<id>/editar/` | `editar_post` | `post_form.html` |
| Eliminar (Delete) | `/posts/<id>/eliminar/` | `eliminar_post` | `post_confirm_delete.html` |

- El listado muestra los posts **publicados** por defecto y tiene filtros para ver borradores, archivados o todos (`?estado=borrador`, `?estado=archivado`, `?estado=todos`).
- Eliminar pide **confirmación**: la página de confirmación se muestra con GET y el post solo se borra al enviar el formulario (POST). También se borra el archivo de su imagen.
- Después de crear o editar, el sitio redirige al detalle del post y muestra un mensaje de confirmación.

### Formulario

`posts/forms.py` define `PostForm`, un `forms.ModelForm` basado en `Post` con los campos `titulo`, `contenido`, `autor`, `estado` e `imagen`. Las views de crear y editar lo instancian con `PostForm(request.POST, request.FILES)` para recibir también la imagen. El `<form>` de `post_form.html` usa `enctype="multipart/form-data"`, necesario para enviar archivos.

### Manejo de imágenes

1. **Campo en el modelo:** `imagen = models.ImageField(upload_to="posts/", null=True, blank=True)`. Es opcional y las imágenes se guardan en `media/posts/`. Migración: `0003_post_imagen.py`.
2. **Dependencia nueva:** `Pillow` (`pip install Pillow`), agregada a `requirements.txt`. Django la necesita para trabajar con `ImageField`.
3. **Configuración en `settings.py`:**
   ```python
   MEDIA_URL = "/media/"
   MEDIA_ROOT = BASE_DIR / "media"
   ```
4. **Servir media en desarrollo** (`blog_project/urls.py`):
   ```python
   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```
5. **En los templates** la imagen se muestra con `{{ post.imagen.url }}` solo si existe (`{% if post.imagen %}`); si un post no tiene imagen, el detalle muestra "Este post no tiene imagen." sin romperse.

Las imágenes subidas quedan en `media/posts/`, que está en `.gitignore` (igual que `db.sqlite3`).

### Cómo probar la carga de imágenes

1. Ejecutar `python manage.py migrate` y `python manage.py runserver`.
2. Entrar a http://127.0.0.1:8000/posts/crear/ (o al botón **Nuevo post**).
3. Completar el formulario, elegir una imagen en **Imagen (opcional)** y poner el estado en **Publicado**.
4. Al guardar, el sitio redirige al detalle, donde se ve la imagen. También aparece como miniatura en el listado.
5. Para cambiarla, entrar a **Editar** y elegir otra imagen. Para quitarla, marcar la casilla **Eliminar** junto a la imagen actual.

## Panel de administración

1. Crear un superusuario (pide nombre de usuario, email y contraseña):

   ```bash
   python manage.py createsuperuser
   ```

2. Levantar el servidor con `python manage.py runserver`.
3. Entrar a http://127.0.0.1:8000/admin/ con ese usuario.
4. En **Posts** se pueden crear, editar y borrar publicaciones. El listado muestra título, autor, estado y fecha de creación, con filtros por estado y fecha, buscador y el estado editable desde la lista (clase `PostAdmin` en `posts/admin.py`).

Al marcar un post como **Publicado**, aparece automáticamente en `/` y en `/posts/`.

## Autor

Ignacio Garcia Fadul
