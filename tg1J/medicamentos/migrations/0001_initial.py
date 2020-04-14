# Generated by Django 2.2.2 on 2020-04-08 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_vencimiento', models.DateField(null=True)),
                ('fabricado_por', models.CharField(max_length=40)),
                ('registro_invima', models.CharField(max_length=40)),
                ('numero_lote', models.CharField(max_length=40)),
                ('presentacion_comercial', models.CharField(blank=True, max_length=40)),
                ('forma_farmaceutica', models.CharField(blank=True, max_length=40)),
                ('principio_activo', models.CharField(blank=True, max_length=40)),
                ('unidad_medica', models.CharField(max_length=40)),
                ('porcentaje', models.CharField(blank=True, max_length=40)),
                ('temperatura', models.CharField(blank=True, max_length=40)),
                ('cantidad', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('asignacionColor', models.CharField(default='Blanco', max_length=30)),
            ],
        ),
    ]
