from django.urls import path
from . import views

urlpatterns = [
    path('paciente/<int:id>/', views.paciente, name='paciente'), 
    path('minhas_consultas/', views.minhas_consultas, name='minhas_consultas'),
    path('consulta/<int:id_consulta>/', views.consulta, name='consulta'), 
]
