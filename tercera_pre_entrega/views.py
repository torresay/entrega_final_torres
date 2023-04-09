from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    params = {}
    return render(request,'home.html',params)