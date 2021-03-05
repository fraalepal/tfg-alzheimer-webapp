from django.urls import path
from . import  views
from django.conf.urls.static import static

urlpatterns=[
     path('register/',views.register, name='register'),
     path('doctor_register/',views.medico_especialista_register.as_view(), name='doctor_register'),
     path('patient_register/',views.paciente_register.as_view(), name='patient_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     
]