from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    user = forms.CharField(widget=forms.TextInput(
                attrs= {
                    'placeholder':'Username'
                }
            ))
    password = forms.CharField(widget=forms.PasswordInput(
                attrs= {
                    'placeholder':'Password'
                }
            ))