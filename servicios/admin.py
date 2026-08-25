from django.contrib import admin
from .models import Servicio

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)