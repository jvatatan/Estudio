# Generated by Django 2.2.2 on 2020-02-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivoMedico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivomedico',
            name='asignacionColor',
            field=models.CharField(default='Blanco', max_length=30),
        ),
    ]