# Generated by Django 3.2.12 on 2022-10-03 11:34

import apps.rendiciones.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0011_alter_rendicion_sitios_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendicion',
            name='img_km_final',
        ),
        migrations.RemoveField(
            model_name='rendicion',
            name='img_km_inicial',
        ),
        migrations.RemoveField(
            model_name='rendicion',
            name='kilometraje_final',
        ),
        migrations.RemoveField(
            model_name='rendicion',
            name='kilometraje_inicial',
        ),
        migrations.AddField(
            model_name='rendiciondetalle',
            name='img_km_final',
            field=models.ImageField(blank=True, null=True, upload_to=apps.rendiciones.models.file_path),
        ),
        migrations.AddField(
            model_name='rendiciondetalle',
            name='img_km_inicial',
            field=models.ImageField(blank=True, null=True, upload_to=apps.rendiciones.models.file_path),
        ),
        migrations.AddField(
            model_name='rendiciondetalle',
            name='kilometraje_final',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rendiciondetalle',
            name='kilometraje_inicial',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
