# Generated by Django 3.2.12 on 2022-10-03 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0021_rename_imagen_rendiciondetalle_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendiciondetalle',
            name='tipo_gasto',
        ),
    ]