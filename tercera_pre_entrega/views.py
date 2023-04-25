from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    params = {}
    return render(request,'index.html',params)

def home(request):
    params = {}
    return render(request,'home.html',params)

def log_in(request):
    
    params = {}

    form = LoginForm()

    params['form'] = form
    params['form'] = form

    #POST
    if request.method == 'POST':
        
        form = LoginForm(request.POST)

        print(form.is_valid())

        if form.is_valid():

            _user = form.cleaned_data['user']

            _password = form.cleaned_data['password']

            user = authenticate(request, username=_user, password=_password)
            

            if user is not None:
                
                auth_login(request, user)
                messages.info(request, 'Has iniciado sesion correctamente!')
                return redirect('home')
            
            else:
                params['invalidate_auth'] = True
                return render(request, 'log_in.html',params)

        return render(request, 'log_in.html', params)

    #GET
    else:

        return render(request,'log_in.html',params)
    


def logout(request):
    
    auth_logout(request)

    messages.info(request, 'Sesion finalizada!')

    return redirect('index')