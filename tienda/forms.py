from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *

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


class DateInput(forms.DateInput):
    input_type = 'date'

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = DataUser
        fields = [
            'first_name',
            'last_name',
            'date_birth',
            'phone',
            'adress',
            'country',
            'state',
            'city',
            'dni',
            'imagen'
        ]
        widgets = {
            'date_birth': DateInput(),
        }


    def __init__(self, *args, **kwargs):
        
        self.request = kwargs.pop("request")

        super(EditProfileForm,self).__init__(*args, **kwargs)

        self.user = self.request.user
        self.dataUser = DataUser.objects.filter(user=self.request.user).get()
        self.fields['first_name'].initial = self.dataUser.first_name
        self.fields['last_name'].initial = self.dataUser.last_name
        self.fields['date_birth'].initial = self.dataUser.date_birth
        self.fields['phone'].initial = self.dataUser.phone
        self.fields['adress'].initial = self.dataUser.adress
        self.fields['country'].initial = self.dataUser.country
        self.fields['state'].initial = self.dataUser.state
        self.fields['city'].initial = self.dataUser.city
        self.fields['dni'].initial = self.dataUser.dni
        self.fields['imagen'].initial = self.dataUser.imagen


class MensajeForm(forms.ModelForm):
    contenido = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Mensaje
        fields = ['contenido']