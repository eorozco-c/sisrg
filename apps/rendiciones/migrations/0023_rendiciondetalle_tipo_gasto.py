# Generated by Django 3.2.12 on 2022-10-03 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0022_remove_rendiciondetalle_tipo_gasto'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendiciondetalle',
            name='tipo_gasto',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, related_name='rendiciones_detalle_tipo_gasto', to='rendiciones.tipodegasto'),
            preserve_default=False,
        ),
    ]
