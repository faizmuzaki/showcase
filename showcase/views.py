from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator
import requests
from .models import *
# Create your views here.

def index(request):
    return render(request, 'showcase/index.html')

def showcase(request):

    # pagination
    p = Paginator(Project.objects.all(), 2)
    page = request.GET.get('page')
    project_list = p.get_page(page)


    return render(request, 'showcase/showcase.html', {
        "projects": project_list
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
