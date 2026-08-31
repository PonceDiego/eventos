from django.urls import path
from . import views
#Llamo a las funciones creadas en las views....
app_name  = 'api'

urlpatterns = [
    path('servicios', views.lista_servicios, name='lista_servicios'),
    path('servicios/<int:servicio_id>', views.detalle_servicio, name='detalle_servicio'),
    path('clientes', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>',views.detalle_cliente, name= 'detalle_cliente'),
    path('coordinadores', views.lista_coordinadores , name='lista_coordinadores' ),
    path('coordinadores/<int:coordinador_id>', views.detalle_coordinador , name='detalle_coordinador'),
    path('empleados',views.lista_empleados, name='lista_empleados'),
    path('empleados/<int:empleado_id>',views.detalle_empleado , name='detalle_empleado')
]