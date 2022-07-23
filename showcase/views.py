from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'showcase/index.html');

def showcase(request):
    return render(request, 'showcase/showcase.html', {
        "projects": Project.objects.all()
    });
def detail(request):
    return render(request, 'showcase/detail.html', {
        "projects": Project.objects.all()
    });