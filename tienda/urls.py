from django.contrib import admin
from django.urls import path
from tienda import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('marcas/', views.marcas, name='marcas'),
    path('cartera/', views.cartera, name='cartera'),
    path('zapato/', views.zapato, name='zapato'),
    path('add_marca', views.add_marca, name='add_marca'),
    path('add_cartera', views.add_cartera, name='add_cartera'),
    path('add_zapato', views.add_zapato, name='add_zapato'),
    path('buscar_marca', views.buscar_marca, name='buscar_marca'),
    path('buscar_cartera', views.buscar_cartera, name='buscar_cartera'),
    path('buscar_zapato', views.buscar_zapato, name='buscar_zapato'),
    #User
    path('register', views.register, name='register'),
]