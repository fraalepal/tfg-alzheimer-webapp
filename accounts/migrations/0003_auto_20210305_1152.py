# Generated by Django 3.0.7 on 2021-03-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210305_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicoespecialista',
            name='consulta',
            field=models.CharField(default=None, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='medicoespecialista',
            name='especialidad',
            field=models.CharField(default=None, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='medicoespecialista',
            name='hospital',
            field=models.CharField(default=None, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='afeccion',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='alergias',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre_cuidador',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='prescripciones',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='requerimentosEspeciales',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono_cuidador',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
