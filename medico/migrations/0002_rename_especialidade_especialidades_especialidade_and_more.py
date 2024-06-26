# Generated by Django 5.0.4 on 2024-04-22 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='especialidades',
            old_name='Especialidade',
            new_name='especialidade',
        ),
        migrations.AddField(
            model_name='especialidades',
            name='icone',
            field=models.ImageField(blank=True, null=True, upload_to='icones'),
        ),
        migrations.AlterField(
            model_name='dadosmedico',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmedico',
            name='especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medico.especialidades'),
        ),
    ]
