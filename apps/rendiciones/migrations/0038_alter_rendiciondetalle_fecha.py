# Generated by Django 3.2.12 on 2022-10-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0037_alter_rendiciondetalle_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendiciondetalle',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
