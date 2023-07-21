from django.shortcuts import render

# Create your views here.

def categoria(request):

    return render(request, 'categoria/categoria.html')

def categorias(request):

    return render(request, 'categoria/categorias.html')
