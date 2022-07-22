from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

card = [
    ["Website Warga Bantu Warga", "Sally Rally"],
    ["Aplikasi Deteksi Dini Gejala Covid-19", "Sally Rally"],
    ["Aplikasi 1", "Sally Rally"],
    ["Aplikasi 2", "Sally Rally"],
    ["Aplikasi 3", "Sally Rally"]
]

def index(request):
    return render(request, 'showcase/index.html');

def showcase(request):
    return render(request, 'showcase/showcase.html', {
        "projects": Project.objects.all()
    });