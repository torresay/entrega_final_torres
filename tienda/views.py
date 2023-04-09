from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def marcas(request):
    
    marcas = Marca.objects.all()
    params = {'marcas':marcas}
    return render(request,'marcas.html', params)

def add_marca(request):

    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            marca = Marca()
            marca.marca = form.cleaned_data['marca']
            marca.pais = form.cleaned_data['pais']
            marca.ano_origen = form.cleaned_data['ano_origen']
            marca.contacto = form.cleaned_data['contacto']
            marca.save()
            form = MarcaForm()
            return redirect('marcas')
    else:
        form = MarcaForm()
    
    params = {'form':form}
    return render(request, 'add_marca.html', params)

def buscar_marca(request):
    form = BuscarMarcaForm(request.POST)
    resultados = []

    if form.is_valid():
        busqueda = form.cleaned_data['marca']
        resultados = Marca.objects.filter(marca__icontains=busqueda)

    params = {'form': form, 'resultados': resultados}

    return render(request, 'buscar_marca.html', params)


def cartera(request):
    carteras = Cartera.objects.all()
    params = {'carteras':carteras}
    return render(request,'cartera.html', params)

def add_cartera(request):

    if request.method == 'POST':
        form = CarteraForm(request.POST)
        if form.is_valid():
            cartera = Cartera()
            cartera.modelo = form.cleaned_data['modelo']
            cartera.marca = form.cleaned_data['marca']
            cartera.fecha_compra = form.cleaned_data['fecha_compra']
            cartera.precio = form.cleaned_data['precio']
            cartera.color = form.cleaned_data['color']
            cartera.dimensiones = form.cleaned_data['dimensiones']
            cartera.save()
            form = CarteraForm()
            return redirect('cartera')
    else:
        form = CarteraForm()
    
    params = {'form':form}
    return render(request, 'add_cartera.html', params)

def buscar_cartera(request):
    form = BuscarCarteraForm(request.POST)
    resultados = []

    if form.is_valid():
        busqueda = form.cleaned_data['modelo']
        resultados = Cartera.objects.filter(modelo__icontains=busqueda)

    params = {'form': form, 'resultados': resultados}
    
    return render(request, 'buscar_cartera.html', params)


def zapato(request):
    zapatos = Zapato.objects.all()
    params = {'zapatos':zapatos}
    return render(request,'zapato.html', params)

def add_zapato(request):

    if request.method == 'POST':
        form = ZapatoForm(request.POST)
        if form.is_valid():
            zapato = Zapato()
            zapato.modelo = form.cleaned_data['modelo']
            zapato.marca = form.cleaned_data['marca']
            zapato.fecha_compra = form.cleaned_data['fecha_compra']
            zapato.precio = form.cleaned_data['precio']
            zapato.color = form.cleaned_data['color']
            zapato.dimensiones = form.cleaned_data['dimensiones']
            zapato.save()
            form = ZapatoForm()
            return redirect('zapato')
    else:
        form = ZapatoForm()
    
    params = {'form':form}
    return render(request, 'add_zapato.html', params)

def buscar_zapato(request):
    form = BuscarZapatoForm(request.POST)
    resultados = []

    if form.is_valid():
        busqueda = form.cleaned_data['modelo']
        resultados = Zapato.objects.filter(modelo__icontains=busqueda)

    params = {'form': form, 'resultados': resultados}
    
    return render(request, 'buscar_zapato.html', params)