# Generated by Django 3.2.12 on 2022-10-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0018_remove_rendiciondetalle_sitios_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendiciondetalle',
            name='sitios_cliente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
