from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
    dni = models.CharField(max_length=9, default="XXXXXXXXX")
    genero = models.CharField(max_length=100, default=None, null=True)
    phone = models.CharField(max_length=9)

class MedicoEspecialista(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, blank=True)
    especialidad = models.CharField(max_length=55, default=None, null=True)
    hospital = models.CharField(max_length=55, default=None, null=True)
    consulta = models.CharField(max_length=55, default=None, null=True)
    is_doctor = True
    is_patient = True

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, blank=True)
    fecha_nacimiento = models.DateField(auto_now_add=True)
    nombre_cuidador = models.CharField(max_length=255, null=True)
    telefono_cuidador = models.CharField(max_length=9, null=True)
    afeccion = models.CharField(max_length=255, default=None, null=True)
    prescripciones = models.CharField(max_length=255, default=None, null=True)
    alergias = models.CharField(max_length=255, default=None, null=True)
    requerimentosEspeciales = models.CharField(max_length=255, default=None, null=True)
    is_doctor = False
    is_patient = True

class CategoriaActividad(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre de categoria")

    


class Actividad(models.Model):
    categoria = models.ForeignKey(CategoriaActividad, verbose_name="categoria", on_delete=models.CASCADE)
    fechaRealización = models.DateTimeField(auto_now_add=True, verbose_name="fecha de realizacion")
    score = models.FloatField(verbose_name="score", default=100.0)


class Informe(models.Model):
    usuario = models.ForeignKey(Paciente, verbose_name="Usuario", on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=255, verbose_name="Observaciones")
    actividades = models.ForeignKey(Actividad, on_delete=models.CASCADE)





