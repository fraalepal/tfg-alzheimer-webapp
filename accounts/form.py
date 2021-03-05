from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, MedicoEspecialista, Paciente

YEARS= [x for x in range(1940,2021)]

class MedicoEspecialistaSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    dni = forms.CharField(required=True)
    genero = forms.ChoiceField(choices=((1, ("Masculino")),
                                        (2, ("Femenino")),
                                        (3, ("Otro"))))
    phone = forms.CharField(required=True)

    #Atributos para medicos especialistas
    especialidad = forms.CharField(required=True)
    hospital = forms.CharField(required=True)
    consulta = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_patient = True
        user.name = self.cleaned_data.get('name')
        user.surname = self.cleaned_data.get('surname')
        user.dni = self.cleaned_data.get('dni')
        user.genero = self.cleaned_data.get('genero')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        medico = MedicoEspecialista.objects.create(user=user)
        medico.especialidad=self.cleaned_data.get('especialidad')
        medico.hospital=self.cleaned_data.get('hospital')
        medico.consulta=self.cleaned_data.get('consulta')
        medico.save()
        return user

class PacienteSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    dni = forms.CharField(required=True)
    enero = forms.ChoiceField(choices=((1, ("Masculino")),
                                        (2, ("Femenino")),
                                        (3, ("Otro"))))
    phone = forms.CharField(required=True)

    #Cosas de paciente
    nombre_cuidador = forms.CharField(required=True)
    telefono_cuidador = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(required=True, label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
    afeccion = forms.CharField(required=True)
    prescripciones = forms.CharField(required=True)
    alergias = forms.CharField(required=True)
    requerimentosEspeciales = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.is_doctor = False
        user.name = self.cleaned_data.get('name')
        user.surname = self.cleaned_data.get('surname')
        user.dni = self.cleaned_data.get('dni')
        user.genero = self.cleaned_data.get('genero')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        paciente = Paciente.objects.create(user=user)
        paciente.fecha_nacimiento=self.cleaned_data.get('fecha_nacimiento')
        paciente.nombre_cuidador=self.cleaned_data.get('nombre_cuidador')
        paciente.telefono_cuidador=self.cleaned_data.get('telefono_cuidador')
        paciente.afeccion=self.cleaned_data.get('afeccion')
        paciente.prescripciones=self.cleaned_data.get('prescripciones')
        paciente.alergias=self.cleaned_data.get('alergias')
        paciente.requerimentosEspeciales=self.cleaned_data.get('requerimentosEspeciales')
        paciente.save()
        return user
