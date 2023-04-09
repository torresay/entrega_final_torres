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



def producto(request):
    params = {}
    return render(request,'productos.html', params)