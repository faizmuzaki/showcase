from django.shortcuts import get_object_or_404
from django.shortcuts import render
import requests
from .models import *
# Create your views here.

def index(request):
    return render(request, 'showcase/index.html')

def showcase(request):
    return render(request, 'showcase/showcase.html', {
        "projects": Project.objects.all()
    })

def detail(request):
    if request.method == 'GET':
        id = request.GET['id']

    project = get_object_or_404(Project, pk=id)
    
    if not project:
        return render(request, 'showcase/showcase.html')
    else:
        return render(request, 'showcase/detail.html', {
            "project": project
        });
