# Blog Django

Proyecto base de un blog web desarrollado con Django (Preentregas 7 y 8).

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
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── lista_posts.html
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

Por ahora los posts del listado son datos de ejemplo definidos en `views.py`; más adelante se van a cargar desde la base de datos con modelos.

## Autor

Ignacio Garcia Fadul
