from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "usuarios/index.html")

def cadastro(request):
    # print(request.META)
    return HttpResponse("Olá, mundo!")

def login(request):
    return render(request, "usuarios/login.html")
