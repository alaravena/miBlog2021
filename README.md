# miBlog2021

Proyecto de Programación web PGY3121 Duoc UC 2021

1) Crear proyecto django
django-admin startproject miBlog
cd miBlog

2) Configuración mínima de settings del proyecto

En el archivo settings configuro a español
LANGUAGE_CODE = 'es'

*) Agregar archivo .gitignore en la raíz del proyecto, se puede usar de ejemplo: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

3) Crear la app de django principal (core)
python manage.py startapp core
agregar la app core a settings en INSTALLED_APPS

4) Templates
Dentro de la app core, crear la carpeta templates y dentro de la carpeta templates crear una carpata core
Siempre en todas las app de django, se debe respetar esta estructura nombreApp/templates/nombreApp
- Creo el template home.html dentro de core/templates/core
- En el archivo views.py que esta en la app core, agrego la función:
def home(request):
    return render(request, 'core/home.html')

5) Agrear Urls
 Agregar el archivo urls.py a la carpeta core con el código 
 from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name="home"),
]

En el archivo urls.py general del proyecto agregan
path('', include('core.urls')),
al urlpatterns
Recuerden importar include, junto con path

6) Archivos Estáticos
Se debe crear una carpeta con la lógica similar a templates nombreApp/static/nombreApp, por ejemplo core/static/core.

Dentro de esta carpeta crear una estructura ordenda con una carpeta css, otra js y otra img. También se puede agregar otra lib para librerías externas.

En el html del template de django, primero se debe cargar los archivos statics de la app
{% load static %}

Luego llamar al recurso usando

{% static 'nombreApp/rut/del/recurso' %}

7) Contexto -> envío de variables al template
Como tercer parámetro de render, en views se puede enviar al template un diccionario con variables, por ejemplo
contexto = {
        'atributo': 'valor'
    }
    return render(request, 'core/home.html', contexto)

Y para llamarlas en el template se utiliza {{ atributp }}
