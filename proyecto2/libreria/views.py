from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "C:/2023-Info-com-8/Django/proyecto2/libreria/templates/paginas/inicio.html")

def nosotros(request):
    return render(request,"C:/2023-Info-com-8/Django/proyecto2/libreria/templates/paginas/nosotros.html")
def libros(request):
    return render(request,"C:/2023-Info-com-8/Django/proyecto2/libreria/templates/libros/index.html")
def crear(request):
    return render(request,"C:/2023-Info-com-8/Django/proyecto2/libreria/templates/libros/crear.html")
def editar(request):
    return render(request,"C:/2023-Info-com-8/Django/proyecto2/libreria/templates/libros/editar.html")