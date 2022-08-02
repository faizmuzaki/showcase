from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
import random
# Create your views here.

def index(request):
    project_list = list(Project.objects.all())
    hl = random.sample(project_list, 3)

    return render(request, 'showcase/index.html', {
        "sample" : hl
    })

def showcase(request):

    ex = False

    if ('search' in request.GET) and (request.GET['search'] != ''):

        q = request.GET['search']

        multi_q = Q(Q(judul__contains=q) | Q(author__nama__contains=q) | Q(author__angkatan__contains=q))
        
        project_list = Project.objects.filter(multi_q)

        if project_list.exists():
            ex = True
    else:
        pq = Project.objects.all()

        if pq.exists():
            ex = True
        # pagination
        p = Paginator(pq, 9)
        page = request.GET.get('page')
        project_list = p.get_page(page)



    return render(request, 'showcase/showcase.html', {
        "projects": project_list,
        "exist" : ex
    })

def detail(request):
    if request.method == 'GET':
        id = request.GET['id']
        if not id.isdigit():
            id = 0

    project = get_object_or_404(Project, pk=id)
    
    if not project:
        return render(request, 'showcase/showcase.html')
    else:
        return render(request, 'showcase/detail.html', {
            "project": project
        });
