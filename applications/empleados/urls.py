from django.urls import path
from . import views

app_name= "persona_app"

urlpatterns = [
    
    path(
        '', 
        views.Inicioview.as_view(), 
        name='inicio'
        ),
    
    path('lista-empleado/',
          views.ListaAllEmpleados.as_view(),
          name = 'empleados_all'
     ),
    path(
          'lista-departamento/<shortname>/',
          views.ListaAllAreaEmpleado.as_view(), 
          name='lista-departamento'
          ),
    path('buscar-empleado/', views.listEmpleadoByKword.as_view()),
    path('Lista-habilidades-empleados/', views.ListhabilidadesempleadosListView.as_view()),
   path(
    'detalle-empleado/<int:pk>/',  # Asegúrate de tener '/' al final y de especificar el tipo de pk.
    views.EmpleadoDetailView.as_view(),
    name='detalle_empleado'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name= 'empleado_add'
        ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
        ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
        ),

    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
        ),

    path(
        'Lista_empleados_admin/', 
        views.ListaEmpleadosAdmin.as_view(), 
        name='empleados_admin'
        ),
    
]
