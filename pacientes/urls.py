from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('escolher_horario/<int:id_dados_medicos>/', views.escolher_horario, name="escolher_horario"),
    path('agendar_horario/<int:id_data_aberta>/', views.agendar_horario, name="agendar_horario"),
    path('minhas_consultas/', views.minhas_consultas, name="minhas_consultas"),
    path('consultas_medico/', views.consultas_medico, name="consultas_medico"),
    path('consulta/<int:id_consulta>/', views.consulta, name="consulta"),
    path('consulta_area_medico/<int:id_consulta>/', views.consulta_area_medico, name="consulta_area_medico"),
    path('add_documento/<int:id_consulta>/', views.add_documento, name="add_consulta"),
    # path('paciente/<int:id>/', views.paciente, name='paciente'), 
    # path('minhas_consultas/', views.minhas_consultas, name='minhas_consultas'),
    # path('consulta/<int:id_consulta>/', views.consulta, name='consulta'), 
]
