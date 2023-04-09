from django.contrib import admin
from django.urls import path
from tienda import views

urlpatterns = [
    path('marcas/', views.marcas, name='marcas'),
    path('producto/', views.producto, name='producto'),
    path('add_marca', views.add_marca, name='add_marca'),
]