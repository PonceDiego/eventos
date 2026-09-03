from rest_framework import serializers
from servicios.models import Servicio , Cliente , Coordinador ,Empleado

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):

        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for f in existing-allowed:
                self.fields.pop(f)

def detalle_generator(tipo):
    detalle = serializers.HyperlinkedIdentityField(
        view_name = f'api:detalle_{tipo}',
        lookup_url_kwarg = f'{tipo}_id'
    )
    return detalle

class ServicioSerializer(DynamicFieldsModelSerializer):
    detalle = detalle_generator("servicio")
    class Meta:
        model = Servicio
        fields = ['detalle', 'id', 'nombre', 'descripcion', 'precio', 'activo']


class ClienteSerializer(DynamicFieldsModelSerializer):
    detalle = detalle_generator("cliente")
    class Meta:
        model = Cliente
        fields= ['detalle', 'id', 'nombre', 'apellido', 'contacto', 'activo']


class CoordinadorSerializer(DynamicFieldsModelSerializer):
    detalle = detalle_generator("coordinador")
    class Meta:
        model = Coordinador
        fields=  ['detalle', 'id', 'nombre', 'apellido', 'dni', 'fecha_alta', 'activo']


class EmpleadoSerializer(DynamicFieldsModelSerializer):
    detalle = detalle_generator("empleado")
    class Meta:
        model = Empleado
        fields=  ['detalle', 'id', 'nombre', 'apellido', 'legajo', 'activo']
