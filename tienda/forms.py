from django import forms
from .models import *

class MarcaForm(forms.Form):
    marca = forms.CharField(max_length=40)
    pais  = forms.CharField(max_length=15)
    ano_origen = forms.IntegerField()
    contacto = forms.EmailField()