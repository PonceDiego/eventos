from django.urls import path

from . import views
from .views import (
    ServicioListView,
    ServicioInactivosListView,
    ServicioCreateView,
    ServicioUpdateView,
    ServicioBajaLogicaView,
    ServicioRestaurarView,
    ClienteListView,
    ClienteInactivoListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteBajaLogicaView,
    ClienteRestaurarView
)

app_name = 'servicios'

urlpatterns = [

    path('', ServicioListView.as_view(), name='listar'),
    path('inactivos/', ServicioInactivosListView.as_view(), name='inactivos'),
    path('nuevo/', ServicioCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', ServicioUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', ServicioBajaLogicaView.as_view(), name='eliminar'),
    path('restaurar/<int:pk>/', ServicioRestaurarView.as_view(), name='restaurar'),

    path('clientes', ClienteListView.as_view(), name='lista_cliente'),
    path('cliente_inactivo/', ClienteInactivoListView.as_view(), name='cliente_inactivo'),
    path('cliente_nuevo/', ClienteCreateView.as_view(), name='cliente_nuevo'),
    path('cliente_editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
    path('cliente_eliminar/<int:pk>/', ClienteBajaLogicaView.as_view(), name='cliente_eliminar'),
    path('cliente_restaurar/<int:pk>/', ClienteRestaurarView.as_view(), name='cliente_restaurar')


]


