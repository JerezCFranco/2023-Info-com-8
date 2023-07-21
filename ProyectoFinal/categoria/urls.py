from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoria, name='Categoria'),
    path('categorias/', views.categorias, name='Categorias'),
]