# Generated by Django 3.2.12 on 2022-10-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0031_remove_rendiciondetalle_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendiciondetalle',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]