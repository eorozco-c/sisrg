# Generated by Django 4.0.3 on 2022-03-21 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0002_rendicion_encargado_alter_rendicion_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rendicion',
            old_name='clientes',
            new_name='cliente',
        ),
    ]