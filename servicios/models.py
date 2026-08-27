from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    descripcion = models.TextField('Descripcion')
    precio = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    activo = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre= models.CharField('Nombre' , max_length=50)
    apellido = models.CharField("Apellido" , max_length=50)
    contacto = models.CharField('contacto' , max_length= 50 , default= '')
    activo = models.BooleanField('Activo' , default=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural  = 'Clientes'

    def __str__(self) :
        return f'{self.nombre} {self.apellido}'


class Coordinadores(models.Model):
    pass

class Empleados(models.Model):
    pass

class ReservasServicios(models.Model):
    pass
