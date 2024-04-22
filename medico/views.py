from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Especialidades, DadosMedico, DatasAbertas
from django.contrib.messages import constants, add_message
from datetime import datetime
from pacientes.models import Consulta

# Create your views here.
def is_medico(user):
    return DadosMedico.objects.filter(user=user).exists()

@login_required
def cadastro_medico(request):
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        return render(request, 'medico/cadastro_medico.html', {'especialidades': especialidades})
    
    #TODO: Validar todos os campos

    elif request.method == "POST":
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')
        if is_medico(request.user):
            add_message(request, constants.WARNING, 'Você já está cadastrado como médico.')
            return redirect('/medicos/abrir_horario')
        dados_medico = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            rg=rg,
            cedula_identidade_medica=cim,
            foto=foto,
            user=request.user,
            descricao=descricao,
            especialidade_id=especialidade,
            valor_consulta=valor_consulta
        )
        dados_medico.save()
        add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso.')
        return redirect('/medicos/abrir_horario')
    
# Se um usuário já for médico não o deixe realizar o cadastro médico novamente:




# def abrir_horario(request):
#     if request.method == "GET":
#         return render(request, "medico/abrir_horario.html")
    
#     if is_medico(request.user):
#         add_message(request, constants.WARNING, 'Você já está cadastrado como médico.')
#         return redirect('abrir_horario')
    
@login_required
def abrir_horario(request):
    if not is_medico(request.user):
        add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')
    if request.method == "GET":
        dados_medicos = DadosMedico.objects.get(user=request.user)
        datas_abertas = DatasAbertas.objects.filter(user=request.user)
        return render(request, 'abrir_horario.html', {'dados_medicos': dados_medicos, 'datas_abertas': datas_abertas})
    elif request.method == "POST":
        data = request.POST.get('data')
        data_formatada = datetime.strptime(data, "%Y-%m-%dT%H:%M")
        
        if data_formatada <= datetime.now():
            add_message(request, constants.WARNING, 'A data deve ser maior ou igual a data atual.')
            return redirect('/medicos/abrir_horario')
        horario_abrir = DatasAbertas(
            data=data,
            user=request.user
        )
        horario_abrir.save()
        add_message(request, constants.SUCCESS, 'Horário cadastrado com sucesso.')
        return redirect('/medicos/abrir_horario')

def consultas_medico(request):
    if not is_medico(request.user):
        add_message(request, constants.WARNING, "Somente médicos podem abrir horários")
        return redirect('/usuarios/sair')
    hoje = datetime.now().date()

    consultas_hoje = Consulta.objects.filter(data_aberta__user=request.user).filter(data_aberta__data__gte=hoje)
    consultas_restantes = Consulta.objects.exclude(id__in=consultas_hoje.values('id'))
    return render(request, 'medico/consultas_medico.html', {'consultas_hoje':consultas_hoje, 'consultas_restantes': consultas_restantes})

def consulta_area_medico(request, id_consulta):
    if not is_medico(request.user):
        add_message(request, constants.WARNING, 'Somente médicos pode abrir horários')
        return redirect('/usuarios/sair')
    if request.method == 'GET':
        consulta = Consulta.objects.get(id=id_consulta)
        return render (request, 'consulta_area_medico.html', {'consulta':consulta})