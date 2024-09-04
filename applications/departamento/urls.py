from django.urls import path
from . import views
app_name= "departamento_app" 
urlpatterns = [
    path('departamento-list/', views.DepartamentoListView.as_view(), name='departamento_lista'),
    
    path(
        'new-departamento/',
         views.NewDepartamentoView.as_view(), 
         name='nuevo_departamento'
         ),
      
]