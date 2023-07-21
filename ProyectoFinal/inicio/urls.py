from django.conf import settings
from django.urls import path
from .models import Categoria, Post
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path('/<categoria_id>/', views.categoria, name="categoria")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)