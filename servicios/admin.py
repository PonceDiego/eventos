from django.contrib import admin
from .models import Servicio , Cliente

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
