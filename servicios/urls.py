from django.urls import path

from . import views
from .views import *

app_name = 'servicios'

urlpatterns = [

    path('', ServicioListView.as_view(), name='listar'),
    path('inactivos/', ServicioInactivosListView.as_view(), name='inactivos'),
    path('nuevo/', ServicioCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', ServicioUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', ServicioBajaLogicaView.as_view(), name='eliminar'),
    path('restaurar/<int:pk>/', ServicioRestaurarView.as_view(), name='restaurar'),

    path('cliente/', ClienteListView.as_view(), name='lista_cliente'),
    path('cliente_inactivo/', ClienteInactivoListView.as_view(), name='cliente_inactivo'),
    path('cliente_nuevo/', ClienteCreateView.as_view(), name='cliente_nuevo'),
    path('cliente_editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
    path('cliente_eliminar/<int:pk>/', ClienteBajaLogicaView.as_view(), name='cliente_eliminar'),
    path('cliente_restaurar/<int:pk>/', ClienteRestaurarView.as_view(), name='cliente_restaurar'),

    path('coordinador/', CoordinadorListView.as_view(), name='lista_coordinador'),
    path('coordinador_inactivo/', CoordinadorInactivoListView.as_view(), name='coordinador_inactivo'),
    path('coordinador_nuevo/', CoordinadorCreateView.as_view(), name='coordinador_nuevo'),
    path('coordinador_editar/<int:pk>/', CoordinadorUpdateView.as_view(), name='coordinador_editar'),
    path('coordinador_eliminar/<int:pk>/', CoordinadorBajaLogicaView.as_view(), name='coordinador_eliminar'),
    path('coordinador_restaurar/<int:pk>/', CoordinadorRestaurarView.as_view(), name='coordinador_restaurar'),


    path('empleado/', EmpleadoListView.as_view(), name='lista_empleados'),
    path('empleado_inactivo/', EmpleadoInactivoListView.as_view(), name='empleado_inactivo'),
    path('empleado_nuevo/', EmpleadoCreateView.as_view(), name='empleado_nuevo'),
    path('empleado_editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_editar'),
    path('empleado_eliminar/<int:pk>/', EmpleadoBajaLogicaView.as_view(), name='empleado_eliminar'),
    path('empleado_restaurar/<int:pk>/', EmpleadoRestaurarView.as_view(), name='empleado_restaurar'),

    path('reservas/', ReservaListView.as_view(), name='lista_reservas'),
    path('reservas/nueva/', ReservaCreateView.as_view(), name='reserva_nuevo'),
    path('reservas/<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva_editar'),
    path('reservas/<int:pk>/eliminar/', ReservaDeleteView.as_view(), name='reserva_eliminar'),


    #ruta de la descripcion del servicio
    path('detalle/<int:pk>/', ServicioDetailView.as_view(), name='detalle'),

]


