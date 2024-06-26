# Generated by Django 5.0.4 on 2024-04-22 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_alter_consulta_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='status',
            field=models.CharField(choices=[('C', 'Cancelada'), ('F', 'Finalizado'), ('I', 'Iniciada'), ('A', 'Agendado')], default='A', max_length=1),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('documento', models.FileField(upload_to='documentos')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pacientes.consulta')),
            ],
        ),
    ]
