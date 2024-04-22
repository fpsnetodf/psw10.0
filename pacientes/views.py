from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
# from medico.views.abrir_horario import is_medico
from medico.models import DadosMedico, DatasAbertas, Especialidades
from .models import Consulta
from django.contrib.messages import add_message, constants

# Create your views here.
def home(request):
    medicos = DadosMedico.objects.all()
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        medico_filtrar = request.GET.get('medico')
        especialidades_filtrar = request.GET.getlist('especialidades')
        if medico_filtrar:
            medicos = medicos.filter(nome__icontains = medico_filtrar)
        if especialidades_filtrar:
            medicos = medicos.filter(especialidade_id__in=especialidades_filtrar)
            return render(request, 'pacientes/home.html', {'medicos': medicos, 'especialidades': especialidades})


def escolher_horario(request, id_dados_medicos):
    if request.method == "GET":
        medico = DadosMedico.objects.get(id=id_dados_medicos)
        datas_abertas = DatasAbertas.objects.filter(user=medico.user).filter(data__gte=datetime.now()).filter(agendado=False)
        return render(request, 'escolher_horario.html', {'medico': medico, 'datas_abertas': datas_abertas})
    
def agendar_horario(request, id_data_aberta):
    if request.method == "GET":
        data_aberta = DatasAbertas.objects.get(id=id_data_aberta)
        horario_agendado = Consulta(
            paciente=request.user,
            data_aberta=data_aberta
        )
        horario_agendado.save()
        # TODO: Sugestão Tornar atomico
        data_aberta.agendado = True
        data_aberta.save()
        add_message(request, constants.SUCCESS, 'Horário agendado com sucesso.')
        return redirect('/pacientes/minhas_consultas/')
    
def minhas_consultas(request):
    if request.method == "GET":
        #TODO: desenvolver filtros
        minhas_consultas = Consulta.objects.filter(paciente=request.user).filter(data_aberta__data__gte=datetime.now())
        return render(request, 'minhas_consultas.html', {'minhas_consultas': minhas_consultas})
    

def consultas_medico(request):
    if not is_medico(request.user):
        add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')
    
    hoje = datetime.now().date()
    consultas_hoje = Consulta.objects.filter(data_aberta__user=request.user).filter(data_aberta__data__gte=hoje).filter(data_aberta__data__lt=hoje + timedelta(days=1))
    consultas_restantes = Consulta.objects.exclude(id__in=consultas_hoje.values('id'))
    return render(request, 'consultas_medico.html', {'consultas_hoje': consultas_hoje, 'consultas_restantes': consultas_restantes, 'is_medico': is_medico(request.user)})
    
# def paciente(request, id):
#     if request.method == 'GET':
#         return HttpResponse(f"O id é: {str(id)}")

# def minhas_consultas(request):
#     minhas_consultas = Consulta.objects.filter(paciente=request.user).filter(data_aberta__data__gte=datetime.now())
#     return render(request, 'pacientes/minhas_consultas.html', {'minhas_consultas': minhas_consultas, })


# def consulta(request, id_consulta):
#     if request.method == 'GET':
#         consulta = Consulta.objects.get(id=id_consulta)
#         dado_medico = DadosMedico.objects.get(user=consulta.data_aberta.user)
#         return render (request,'pacientes/consulta.html', {'consulta': consulta, 'dado_medico': dado_medico})
    





