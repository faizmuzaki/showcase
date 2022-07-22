from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'showcase/index.html');

def showcase(request):
    return render(request, 'showcase/showcase.html');