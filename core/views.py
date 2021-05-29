from django.shortcuts import render

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()

# Create your views here.
def home(request):
    lista = ["Chocolate", "Helado", "Humitas"]

    hijo = Persona("Darth Vento Colitaparada", '1,5')

    contexto = {
        'nombre': 'Alejandra Aravena',
        'edad': 42,
        'comidas': lista,
        'hijo': hijo
    }
    return render(request, 'core/home.html', contexto)
