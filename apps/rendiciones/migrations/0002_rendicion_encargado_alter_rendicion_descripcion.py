# Generated by Django 4.0.3 on 2022-03-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendicion',
            name='encargado',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rendicion',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
