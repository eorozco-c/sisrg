# Generated by Django 3.2.12 on 2022-09-28 12:32

import apps.rendiciones.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0008_auto_20220927_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendiciondetalle',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=apps.rendiciones.models.file_path),
        ),
        migrations.AlterField(
            model_name='rendicion',
            name='img_km_final',
            field=models.ImageField(blank=True, null=True, upload_to=apps.rendiciones.models.file_path),
        ),
        migrations.AlterField(
            model_name='rendicion',
            name='img_km_inicial',
            field=models.ImageField(blank=True, null=True, upload_to=apps.rendiciones.models.file_path),
        ),
    ]
