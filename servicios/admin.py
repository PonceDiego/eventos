from django.contrib import admin
from .models import Servicio, Cliente, Coordinador, Empleado, ReservaServicios , ObjetivoVenta
from django.contrib.auth.models import User, Group


# Título de la barra superior
admin.site.site_header = "Administración de EventosApp"

# Texto en la pestaña del navegador
admin.site.site_title = "Eventos Admin"

# Subtítulo de la página principal
admin.site.index_title = "Panel de control"

# Removiendo modelos por defecto
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'activo')
    search_fields = ('nombre' , 'apellido')
    list_filter = ('activo',)

@admin.register(Coordinador)
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'dni' , 'fecha_alta', 'activo')
    search_fields = ('nombre' , 'apellido')
    list_filter = ('activo',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'legajo', 'activo')
    search_fields = ('nombre' , 'apellido')
    list_filter = ('activo',)

@admin.register(ReservaServicios)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('fecha_servicio', 'cliente', 'coordinador', 'fecha_reserva')


@admin.register(ObjetivoVenta)
class ObjetivoVentaAdmin(admin.ModelAdmin):
    list_display = ('servicio', 'meta', 'activo')
    search_fields = ('servicio__nombre',)
    list_filter = ('activo',)