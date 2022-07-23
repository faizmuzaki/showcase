import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('showcase', views.showcase, name='showcase'),
    path('detail', views.detail, name='detail')
]
