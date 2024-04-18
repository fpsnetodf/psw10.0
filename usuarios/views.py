from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.messages import constants, add_message


# Create your views here.

def home(request):
    return render(request, "usuarios/index.html")

def cadastro(request):
    # print(request.META)
    return HttpResponse("Olá, mundo!")

def login_view(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get("senha")
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
            return redirect('/pacientes/home')
        return redirect('/login')

