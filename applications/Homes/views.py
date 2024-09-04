from django.shortcuts import render
from django.shortcuts import render
from .models import Prueba
from django.views.generic import TemplateView, ListView, CreateView
from .forms import PruebaForm  



class IndexView(TemplateView):
    template_name = "home/home.html"

    
class ResumenFoundationview(TemplateView):
    template_name = "home/resumen_fouendation.html"


class PruebaListView(ListView):
    
    template_name = "home/lista.html"
    queryset = ['A', 'B','C']
    context_object_name= 'Lista_prueba'


class modelopruebaListView(ListView):
    model = Prueba
    template_name = "home/prueba.html"
    context_object_name = 'list_prueba'


class pruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'

