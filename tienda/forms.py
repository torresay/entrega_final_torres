from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *

# class MarcaForm(forms.Form):
#     marca = forms.CharField(max_length=40)
#     pais  = forms.CharField(max_length=15)
#     ano_origen = forms.IntegerField()
#     contacto = forms.EmailField()
#     imagen = forms.ImageField()

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['marca', 'pais', 'ano_origen', 'contacto', 'imagen']
class CarteraForm(forms.ModelForm):
    class Meta:
        model = Cartera
        fields = ['modelo', 'marca', 'fecha_compra', 'precio', 'color', 'dimensiones', 'imagen']

class ZapatoForm(forms.ModelForm):
    class Meta:
        model = Zapato
        fields = ['modelo', 'marca', 'fecha_compra', 'precio', 'color', 'dimensiones', 'imagen']
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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
                    ]
                    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True