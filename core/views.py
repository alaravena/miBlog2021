from django.shortcuts import render

# Create your views here.
def home(request):
    lista = ["Chocolate", "Helado", "Humitas"]
    contexto = {
        'nombre': 'Alejandra Aravena',
        'edad': 42,
        'comidas': lista
    }
    return render(request, 'core/home.html', contexto)
