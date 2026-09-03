from django.urls import path
from django.views.generic import RedirectView, TemplateView
from . import views

app_name  = 'api'

urlpatterns = [
    # Landing Page de la API
    path('', TemplateView.as_view(template_name='api/index.html'), name='index'),

    # Redirecciones 
    path('servicios/', RedirectView.as_view(pattern_name='api:lista_servicios', permanent=True)),
    path('clientes/', RedirectView.as_view(pattern_name='api:lista_clientes', permanent=True)),
    path('coordinadores/', RedirectView.as_view(pattern_name='api:lista_coordinadores', permanent=True)),
    path('empleados/', RedirectView.as_view(pattern_name='api:lista_empleados', permanent=True)),

    # Llamo a las funciones creadas en las views....
    path('servicios', views.lista_servicios, name='lista_servicios'),
    path('servicios/<int:servicio_id>', views.detalle_servicio, name='detalle_servicio'),

    path('clientes', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>',views.detalle_cliente, name= 'detalle_cliente'),

    path('coordinadores', views.lista_coordinadores , name='lista_coordinadores' ),
    path('coordinadores/<int:coordinador_id>', views.detalle_coordinador , name='detalle_coordinador'),

    path('empleados',views.lista_empleados, name='lista_empleados'),
    path('empleados/<int:empleado_id>',views.detalle_empleado , name='detalle_empleado')
]