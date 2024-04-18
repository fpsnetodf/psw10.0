from django.shortcuts import render

# Create your views here.
def cadastro_medico(request):
    return render(request, 'medico/cadastro_medico.html')

def abrir_horario(request):
    return render(request, "medico/abrir_horario.html")