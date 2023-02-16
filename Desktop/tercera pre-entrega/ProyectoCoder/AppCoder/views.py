from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def compra(request):
    return render(request, 'AppCoder/compra.html')

def vendedor(request):
    return render(request, 'AppCoder/vendedor.html')

def cliente(request):
    return render(request, 'AppCoder/cliente.html')

