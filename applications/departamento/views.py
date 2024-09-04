from django.shortcuts import render
from django.views.generic import ListView  # Importa ListView desde django.views.generic
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.empleados.models import Empleado
from .models import Departamento
# Create your views here.


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/' 

    def form_valid(self, form):
        # Imprimir los datos del formulario para depuración
        print("Datos limpiados:", form.cleaned_data)

        try:
            # Crear el nuevo departamento
            depa = Departamento(
                name=form.cleaned_data['departamento'],  
                short_name=form.cleaned_data['shortname']  
            )
            depa.save()
            print("Departamento guardado:", depa)

            # Crear el nuevo empleado
            nombre = form.cleaned_data['nombre']  
            apellido = form.cleaned_data['apellido']  
            Empleado.objects.create(
                first_name=nombre,
                last_name=apellido,
                job='1',  
                departamento=depa
            )
            print("Empleado guardado con nombre:", nombre, "y apellido:", apellido)

            # Si todo va bien, redirige a la URL de éxito
            return super().form_valid(form)
        
        except Exception as e:
            # Imprimir error en caso de excepción
            print("Error al guardar:", e)
            return self.form_invalid(form)
        


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'

        





