from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy

class Schoollist(ListView):
    model=School
    context_object_name='allso'
    template_name='app/schoollist.html'


class SchoolDetail(DetailView):
    model=School
    context_object_name='DOSI'
    
class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='dso'
    success_url=reverse_lazy('Schoollist')