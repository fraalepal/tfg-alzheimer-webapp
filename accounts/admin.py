from django.contrib import admin
from .models import MedicoEspecialista, Paciente, User

admin.site.register(User)
admin.site.register(MedicoEspecialista)
admin.site.register(Paciente)
