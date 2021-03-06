# Generated by Django 4.0.3 on 2022-03-21 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estados', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rendicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rendiciones_cliente', to='clientes.cliente')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rendiciones_nombre_estado', to='estados.nombre_estado')),
                ('sitios_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rendiciones_sitios_cliente', to='clientes.sitios_cliente')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rendiciones_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
