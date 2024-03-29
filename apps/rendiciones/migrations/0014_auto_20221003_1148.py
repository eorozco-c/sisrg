# Generated by Django 3.2.12 on 2022-10-03 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rendiciones', '0013_auto_20221003_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeGasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='rendiciondetalle',
            name='tipo_gasto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='rendiciones_detalle_tipo_gasto', to='rendiciones.tipodegasto'),
            preserve_default=False,
        ),
    ]
