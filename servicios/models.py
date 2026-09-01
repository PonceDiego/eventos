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


class Coordinador(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    dni = models.IntegerField('Dni' )
    fecha_alta = models.DateTimeField('Fecha_Alta' , auto_now_add=True)
    activo = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Coordinador'
        verbose_name_plural  = 'coordinadores'

    def __str__(self) :
        return f'{self.nombre} {self.apellido}'


class Empleado(models.Model):
    nombre = models.CharField('Nombre' , max_length=50)
    apellido = models.CharField('Apellido' , max_length=50)
    legajo = models.IntegerField('Legajo')
    activo = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural  = 'empleados'

    def __str__(self) :
        return f'{self.nombre} {self.apellido}'

class ReservaServicios(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name = 'reservas')
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE, related_name= 'reservas')
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name='reservas_empleado')
    coordinador = models.ForeignKey('Coordinador', on_delete=models.CASCADE, related_name='reservas_coordinador')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_servicio = models.DateTimeField()

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f"Reserva de {self.servicio} - {self.cliente} - ({self.fecha_reserva.strftime('%dd/%mm/%YYYY')})"


class ObjetivoVenta(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='objetivos')
    meta = models.PositiveIntegerField('Meta de ventas')
    activo = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Objetivo de venta'
        verbose_name_plural = 'Objetivos de venta'

    def __str__(self):
        return f'{self.servicio.nombre} - Meta: {self.meta}'