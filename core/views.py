from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'nombre': 'Alejandra Aravena',
        'edad': 42
    }
    return render(request, 'core/home.html', contexto)
