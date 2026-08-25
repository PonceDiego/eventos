from django.db import models

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    descripcion = models.TextField('Descripcion')
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    activo = models.BooleanField('Activo', default=True)
    creado_el = models.DateTimeField('Fecha de creacion', auto_now_add=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    pass

class Coordinadores(models.Model):
    pass

class Empleados(models.Model):
    pass

class ReservasServicios(models.Model):
    pass
