# Generated by Django 3.2.12 on 2022-10-03 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0011_alter_rendicion_sitios_cliente'),
        ('clientes', '0002_alter_sitios_cliente_cliente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sitios_cliente',
        ),
    ]
