from rest_framework import serializers
from servicios.models import Servicio , Cliente , Coordinador ,Empleado


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields= '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields= '__all__'


class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields= '__all__'


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields= '__all__'
