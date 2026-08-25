from django.urls import path
from .views import (
    ServicioListView,
    ServicioInactivosListView,
    ServicioCreateView,
    ServicioUpdateView,
    ServicioBajaLogicaView,
    ServicioRestaurarView
)

app_name = 'servicios'

urlpatterns = [

    path('', ServicioListView.as_view(), name='listar'),
    path('inactivos/', ServicioInactivosListView.as_view(), name='inactivos'),
    path('nuevo/', ServicioCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', ServicioUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', ServicioBajaLogicaView.as_view(), name='eliminar'),
    path('restaurar/<int:pk>/', ServicioRestaurarView.as_view(), name='restaurar'),

]