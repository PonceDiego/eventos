from django.contrib import admin
from .models import Servicio, Cliente, Coordinador, Empleado


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
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'dni' , 'fecha_alta')
    search_fields = ('nombre' , 'apellido')
    list_filter = ('activo',)


@admin.register(Empleado)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'legajo')
    search_fields = ('nombre' , 'apellido')
    list_filter = ('activo',)