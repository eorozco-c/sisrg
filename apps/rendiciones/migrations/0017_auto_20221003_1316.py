# Generated by Django 3.2.12 on 2022-10-03 13:16

import apps.rendiciones.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0016_delete_tipodegasto'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeGasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='rendicion',
            name='sitios_cliente',
        ),
        migrations.RemoveField(
            model_name='rendiciondetalle',
            name='imagen',
        ),
        migrations.AddField(
            model_name='rendiciondetalle',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to=apps.rendiciones.models.file_path_detalle),
        ),
        migrations.AddField(
            model_name='rendiciondetalle',
            name='sitios_cliente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rendiciondetalle',
            name='tipo_gasto',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, related_name='rendiciones_detalle_tipo_gasto', to='rendiciones.tipodegasto'),
            preserve_default=False,
        ),
    ]