from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Especialidades, DadosMedico
from django.contrib.messages import constants, add_message

# Create your views here.
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
    
def is_medico(user):
    return DadosMedico.objects.filter(user=user).exists()



def abrir_horario(request):
    if request.method == "GET":
        return render(request, "medico/abrir_horario.html")
    
    if is_medico(request.user):
        add_message(request, constants.WARNING, 'Você já está cadastrado como médico.')
        return redirect('abrir_horario')
    
@login_required
def abrir_horario(request):
    if not is_medico(request.user):
        add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')
    if request.method == "GET":
        dados_medicos = DadosMedico.objects.get(user=request.user)
        return render(request, 'medico/abrir_horario.html', {'dados_medicos': dados_medicos})
        #return render(request, 'medico/abrir_horario.html')
