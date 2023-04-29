from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, UpdateView
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
def about(request):
    params = {}
    return render(request,'about.html',params)


def marcas(request):
    
    marcas = Marca.objects.all()
    params = {'marcas':marcas,'MEDIA_URL': settings.MEDIA_URL}
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
            marca.imagen = form.cleaned_data['imagen']
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

def editMarca(request, marca_id):
    _marca = Marca.objects.get(id=marca_id)
    form = MarcaForm(instance=_marca, data=request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('marcas')

    params = {'form':form}
    return render(request, 'edit_marca.html', params)

    

# def deleteMarca(request, marca_id):
    
#     marca = Marca.objects.get(pk=marca_id)
#     marca.delete()
#     account_id = transaction.wallet.account.id
#     messages.success(request, 'Has borrado la marca exitosamente!')
    
#     return redirect('marca', account_id=account_id)

def cartera(request):
    carteras = Cartera.objects.all()
    params = {'carteras':carteras,'MEDIA_URL': settings.MEDIA_URL}
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
            cartera.imagen = form.cleaned_data['imagen']
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


def editCartera(request, cartera_id):
    _cartera = Cartera.objects.get(id=cartera_id)
    form = CarteraForm(instance=_cartera, data=request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cartera')

    params = {'form':form}
    return render(request, 'edit_cartera.html', params)


def zapato(request):
    zapatos = Zapato.objects.all()
    params = {'zapatos':zapatos,'MEDIA_URL': settings.MEDIA_URL}
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
            zapato.imagen = form.cleaned_data['imagen']
            zapato.save()
            form = ZapatoForm()
            return redirect('zapato')
    else:
        form = ZapatoForm()
    
    params = {'form':form}
    return render(request, 'add_zapato.html', params)


def editZapato(request, zapato_id):

    _zapato = Zapato.objects.get(id=zapato_id)

    form = ZapatoForm(instance=_zapato, data=request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('zapato')

    params = {'form':form}
    return render(request, 'edit_zapato.html', params)


def buscar_zapato(request):

    form = BuscarZapatoForm(request.POST)

    resultados = []

    if form.is_valid():
        busqueda = form.cleaned_data['modelo']
        resultados = Zapato.objects.filter(modelo__icontains=busqueda)

    params = {'form': form, 'resultados': resultados}
    
    return render(request, 'buscar_zapato.html', params)


def register(request):
    params = {}

    form = CreateUserForm()

    params['form'] = form

    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)

        params['form'] = form
        
        print(form.is_valid())

        if form.is_valid():
            
            form.save()
        
            return redirect('login')
        
        else:
        
            return render(request,'register.html',params)

    else:
        return render(request,'register.html',params)
    

@login_required(login_url='/login/')
def logout(request):
    
    auth_logout(request)

    messages.info(request, 'You have successfully log out!')

    return redirect('home')