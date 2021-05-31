# miBlog2021

Proyecto de Programación web PGY3121 Duoc UC 2021

## Para usar este repositorio

Descargar o clonar, luego ejecutar la instalación de los paquetes de **requirements.txt** con:

```bash
pip install -r requirements.txt
```

### Para crear el archivo requirements.txt

Antes de enviar su propio proyecto, en la raíz del proyecto debe ejecutar:

```bash
pip freeze > requirements.txt
```

## Crear proyecto django

Por consola

```bash
django-admin startproject miBlog
```

Desde este punto en adelante siempre se debe trabajar dentro de la carpeta del proyecto

```tree
miBlog
│   manage.py      
│   .gitignore     
│
└───miBlog
│   │   settings.py
│   │   urls.py
│ (..y mas)
```

### Agregar archivo .gitignore

En la raíz del proyecto, antes de subir al repositorio por primera vez.

Se puede usar de ejemplo: <https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/>

## 1.- Configuración mínima de settings del proyecto

En el archivo settings del proyecto configuro a español

```python
LANGUAGE_CODE = 'es'
```

### Primer migrate

Para crear las bases de datos básicas propias de django

```bash
python manage.py migrate
```

### Levantar el servidor

```bash
python manage.py runserver
```

## 2.- Crear la app de django principal (core)

```bash
python manage.py startapp core
```

Agregar la app core a settings en la lista:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

## 3.- Templates

Dentro de la app core, crear la carpeta templates y dentro de la carpeta templates crear una carpata core

```tree
miBlog    
└───core
│   └───templates
│       └───core
```

Siempre en todas las app de django, se debe respetar esta estructura *nombreApp/templates/nombreApp*

### 1) Creo el template

Por ejemplo home.html dentro de core/templates/core

```tree
└───core
│   │   views.py 
│   └───templates
│       └───core
│           │   home.html 
```

### 2) Agrego función en views.py

Que esta en la app core, agrego la función:

```python
def home(request):
    return render(request, 'core/home.html')
```

### 3) Agrear Urls

Agregar el archivo urls.py a la carpeta core

```tree
└───core
│   │   urls.py
│   │   views.py 
│   └───templates
│       └───core
│           │   home.html 
```

Con el código:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name="home"),
]
```

#### Archivo urls.py general

Donde están los settings del proyecto, también está el archivo central de urls, se debe agregar:

```python
path('', include('core.urls')),
```

Al listado de urlpatterns
Recuerden importar include, en la misma linea de path

## 4.- Archivos Estáticos

Se debe crear una carpeta con la lógica similar a templates *nombreApp/static/nombreApp*.
Dentro de esta carpeta crear una estructura ordenda con una carpeta css, otra js y otra img. También se puede agregar otra lib para librerías externas, etc.

```tree
└───core
│   │   urls.py
│   │   views.py 
│   │
│   └───templates
│   │   └───core
│   │       │   home.html 
│   │       
│   └───static
│       └───core
│           └───css
│           └───img
│           └───js
```

### Cargar archivos static en el template

En el html del template de django, primero se debe indicar

```js
{% load static %}

```

Luego llamar al recurso usando

```js
{% static 'nombreApp/rut/del/recurso' %}
```

## 5.- Envío de variables

Se utiliza desde el *views.py* en el tercer parámetro del render, llamado contexto, que es de tipo diccionario

```python
contexto = {
        'atributo': 'valor'
    }
    return render(request, 'core/home.html', contexto)
```

Y para llamarlas en el template se utiliza `{{ atributo }}`

## 6.- Templates complejas

En el template *blog.html* tenemos un ejemplo complejo de estructura html que requiere que se utilice archivos estáticos. Utilizando la platilla de <https://github.com/StartBootstrap/startbootstrap-clean-blog>. En el caso del proyecto semestral se debe tomar los html trabajados en unidades anteriores.

- Primero se copia todo el código al archivo html dentro del sistema de templates de django.
- Todos los archivos estáticos como css, js, imágenes y librerías que se llaman de forma local, se trasladan a las carpetas correspondientes dentro de static.
- En el html del template se reemplaza todas las llamadas a archivos locales por el sistema de enrutamiento static
- Se agrega la función que renderea el template en *views.py*
- Se agrega la ruta que corresponda en *urls.py*

[//]: # (Collectstatic)
