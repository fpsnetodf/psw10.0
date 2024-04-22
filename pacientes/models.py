from django.db import models
from django.contrib.auth.models import User
from medico.models import DatasAbertas
from datetime import datetime

# Create your models here.

class Consulta(models.Model):
    status_choices = {
        ('A', 'Agendado'),
        ('F', 'Finalizado'),
        ('C', 'Cancelada'),
        ('I', 'Iniciada')
    }
    paciente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_aberta = models.ForeignKey(DatasAbertas, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_choices, default='A')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.paciente.username
    
    def proxima_data(self):
        proxima_data = DatasAbertas.objects.filter(user=self.user).filter(data__gt=datetime.now()).filter(agendado=False).order_by('data').first()

class Documento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    documento = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.titulo