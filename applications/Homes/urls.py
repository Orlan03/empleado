from django.urls import path
from . import views 
urlpatterns = [
    
   path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('modelo/', views.modelopruebaListView.as_view()),
    path('add/', views.pruebaCreateView.as_view()),
    path(
        'resumen_foundation/',
        views.ResumenFoundationview.as_view(),
        name = 'Resuemn_foundation'
    ),



   
]