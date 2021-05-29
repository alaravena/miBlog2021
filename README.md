# miBlog2021

Proyecto de Programación web PGY3121 Duoc UC 2021

1) Crear proyecto django
django-admin startproject miBlog
cd miBlog

2) Configuración mínima de settings del proyecto

En el archivo settings configuro a español
LANGUAGE_CODE = 'es'

3) Crear la app de django principal (core)
python manage.py startapp core
agregar la app core a settings en INSTALLED_APPS