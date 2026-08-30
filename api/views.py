from rest_framework.decorators import api_view
from rest_framework.response import Response
from servicios.models import Servicio, Cliente, Coordinador , Empleado
from .serializers import ServicioSerializer, ClienteSerializer , CoordinadorSerializer ,EmpleadoSerializer
from django.shortcuts import  get_object_or_404


# Create your views here.
#SERVICIO
@api_view(['GET'])
def lista_servicios(request):
    servicios = Servicio.objects.all()
    serializer = ServicioSerializer(servicios , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_servicio(request,servicio_id):
    servicio=get_object_or_404(Servicio , pk = servicio_id)
    serializer= ServicioSerializer(servicio)
    return Response(serializer.data)

#CLIENTE
@api_view(['GET'])
def lista_clientes(request):
    clientes = Cliente.objects.all()
    serializer= ClienteSerializer(clientes , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_cliente(request,cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    serializer= ClienteSerializer(cliente)
    return Response(serializer.data)

#COORDINADOR
@api_view(['GET'])
def lista_coordinadores(request):
    coordinadores= Coordinador.objects.all()
    serializer = CoordinadorSerializer(coordinadores , many=True)
    return  Response(serializer.data)

@api_view(['GET'])
def detalle_coordinador(request, coordinador_id):
    coordinador = get_object_or_404(Coordinador , pk = coordinador_id)
    serializer = CoordinadorSerializer(coordinador)
    return Response(serializer.data)

#EMPLEADO
@api_view(['GET'])
def lista_empleados(request):
    empleados= Empleado.objects.all()
    serializer= EmpleadoSerializer(empleados , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_empleado(request,empleado_id):
    empleado=get_object_or_404(Empleado, pk = empleado_id)
    serializer = EmpleadoSerializer(empleado)
    return Response(serializer.data)