# Generated by Django 3.2.12 on 2022-10-03 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0017_auto_20221003_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendiciondetalle',
            name='sitios_cliente',
        ),
    ]
