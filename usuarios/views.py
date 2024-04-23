from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.messages import constants, add_message


# Create your views here.

def home(request):
    return render(request, "usuarios/index.html")

def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')
        users = User.objects.filter(username=username)
        if users.exists():
            print('Erro 1')
            return redirect('/usuarios/cadastro')
        if senha != confirmar_senha:
            print('Erro ')
            return redirect('/usuarios/cadastro.')
        if len(senha) < 6:
            print('Erro 3')
            return redirect('/usuarios/cadastro')

        try:
            User.objects.create_user(
            username=username,
            email=email,
            password=senha
            )
            return redirect('/usuarios/login')
        except:
            print('Erro 4')
            return redirect('/usuarios/cadastro')

def login_view(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get("senha")
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('/pacientes/home')
        
        add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/login')

def sair(request):
    logout(request)
    return redirect('/usuarios/login')