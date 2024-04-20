from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from medico.views.abrir_horario import is_medico
from medico.models import DadosMedico
from .models import Consulta

# Create your views here.
def paciente(request, id):
    if request.method == 'GET':
        return HttpResponse(f"O id é: {str(id)}")
    

def minhas_consultas(request):
    minhas_consultas = Consulta.objects.filter(paciente=request.user).filter(data_aberta__data__gte=datetime.now())
    return render(request, 'pacientes/minhas_consultas.html', {'minhas_consultas': minhas_consultas, })


def consulta(request, id_consulta):
    if request.method == 'GET':
        consulta = Consulta.objects.get(id=id_consulta)
        dado_medico = DadosMedico.objects.get(user=consulta.data_aberta.user)
        return render (request,'pacientes/consulta.html', {'consulta': consulta, 'dado_medico': dado_medico})


