from django import forms
from .models import *

class MarcaForm(forms.Form):
    marca = forms.CharField(max_length=40)
    pais  = forms.CharField(max_length=15)
    ano_origen = forms.IntegerField()
    contacto = forms.EmailField()

class CarteraForm(forms.Form):
    modelo = forms.CharField(max_length=40)
    marca = forms.ModelChoiceField(Marca.objects.all())
    fecha_compra = forms.DateField()
    precio = forms.FloatField()
    color = forms.CharField(max_length=15)
    dimensiones = forms.CharField(max_length=20)

class ZapatoForm(forms.Form):
    modelo = forms.CharField(max_length=40)
    marca = forms.ModelChoiceField(Marca.objects.all())
    fecha_compra = forms.DateField()
    precio = forms.FloatField()
    color = forms.CharField(max_length=15)
    dimensiones = forms.CharField(max_length=20)

class BuscarMarcaForm(forms.Form):
    marca = forms.CharField(
        label='Buscar Marca',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la marca a buscar...'}),
        max_length=20
    )

class BuscarCarteraForm(forms.Form):
    modelo = forms.CharField(
        label='Buscar Cartera',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la cartera a buscar...'}),
        max_length=20
    )

class BuscarZapatoForm(forms.Form):
    modelo = forms.CharField(
        label='Buscar Zapato',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el zapato a buscar...'}),
        max_length=20
    )