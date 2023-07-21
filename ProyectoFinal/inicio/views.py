from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.

def inicio(request):

    posts=Post.objects.all()
    return render(request, 'inicio/inicio.html', {'posts': posts})

def categoria(request, categoria_id):
    
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    created=Post.objects.order_by('-created')
    return render(request, "categoria/categoria.html/", {"categoria": categoria, "posts": posts , 'created':created})
