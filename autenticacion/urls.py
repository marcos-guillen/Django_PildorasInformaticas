from django.urls import path
from .views import VRegistro, cerrar_sesion,logear


urlpatterns = [
    path('logout',cerrar_sesion, name='CerrarSession'),
    path('logear',logear, name='Login'),
    path('',VRegistro.as_view(), name='Autenticacion'),
]
