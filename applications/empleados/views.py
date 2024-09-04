from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    )
# Create your views here.

from .models import Empleado
from .forms import EmpleadoForm


class Inicioview(TemplateView):
    #pagina de inicio
    template_name = "inicio.html"


class ListaAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    model = Empleado
    paginate_by = 5
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista
    
class ListaEmpleadosAdmin(ListView):
    template_name = 'empleado/lista_empleados.html'
    model = Empleado
    paginate_by = 5
    context_object_name = 'empleados'

    

#lista empleado de una area 
class ListaAllAreaEmpleado(ListView):
    template_name = 'empleado/list_all_departamento.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista
    
class listEmpleadoByKword(ListView):
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):

        print("************************")
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name= palabra_clave
        )
        print ('lista resultado:', lista)
        return lista



class ListhabilidadesempleadosListView(ListView):
    template_name = "empleado/habilidadesempleados.html"
    context_object_name = 'empleado'
    
    def get_queryset(self):
        # Obtener el ID del parámetro GET
        empleado_id = self.request.GET.get('kword', None)
        # Si se proporciona un ID, filtra por ID; de lo contrario, devuelve una lista vacía
        if empleado_id:
            return Empleado.objects.filter(id=empleado_id)
        return Empleado.objects.none()
    


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detalle_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    
       

class SuccessView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save()
        print(empleado)
        empleado.full_name = empleado.first_name +' ' + empleado.last_name 
        return super().form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/update.html"
    fields = ['first_name', 
              'last_name', 
              'job', 
              'departamento', 
              'habilidades', 
     ]
    success_url = reverse_lazy('persona_app:empleados_admin')
   
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('********************Metodo Post *******************')

        return super().post(request, *args, **kwargs)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


