from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from servicios.models import Servicio, Cliente, Coordinador , Empleado
from .serializers import ServicioSerializer, ClienteSerializer , CoordinadorSerializer ,EmpleadoSerializer


# Create your views here.
#SERVICIO
@api_view(['GET'])
def lista_servicios(request):
    servicios = Servicio.objects.all()
    serializer = ServicioSerializer(servicios , many=True, context={'request' : request})
    return Response(serializer.data)

@api_view(['GET'])
def detalle_servicio(request,servicio_id):
    try:
        servicio = Servicio.objects.get(pk=servicio_id)
    except Servicio.DoesNotExist:
        return Response(
            {"razón": f"No existe un servicio asociado al id número {servicio_id}."}, 
            status=status.HTTP_404_NOT_FOUND
        )
    sin_detalle = ['id', 'nombre', 'descripcion', 'precio', 'activo']
    serializer= ServicioSerializer(servicio,
        fields = sin_detalle,
        context={'request' : request})
    return Response(serializer.data)

#CLIENTE
@api_view(['GET'])
def lista_clientes(request):
    clientes = Cliente.objects.all()
    serializer= ClienteSerializer(clientes , many=True, context={'request' : request})
    return Response(serializer.data)

@api_view(['GET'])
def detalle_cliente(request,cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        return Response(
            {"razón": f"No existe un cliente asociado al id número {cliente_id}."},
            status = status.HTTP_404_NOT_FOUND
        )
    sin_detalle = ['id', 'nombre', 'apellido', 'contacto', 'activo']
    serializer= ClienteSerializer(cliente,
        fields = sin_detalle,
        context={'request' : request})
    return Response(serializer.data)

#COORDINADOR
@api_view(['GET'])
def lista_coordinadores(request):
    coordinadores= Coordinador.objects.all()
    serializer = CoordinadorSerializer(coordinadores , many=True, context={'request' : request})
    return  Response(serializer.data)

@api_view(['GET'])
def detalle_coordinador(request, coordinador_id):
    try:

        coordinador = Coordinador.objects.get(pk = coordinador_id)
    except Coordinador.DoesNotExist:
        return Response(
            {"razón": f"No existe un coordinador asociado al id número {coordinador_id}."},
            status = status.HTTP_404_NOT_FOUND
        )
    sin_detalle = ['id', 'nombre', 'apellido', 'dni', 'fecha_alta', 'activo']
    serializer= CoordinadorSerializer(coordinador,
            fields = sin_detalle,
            context={'request' : request})
    return Response(serializer.data)

#EMPLEADO
@api_view(['GET'])
def lista_empleados(request):
    empleados= Empleado.objects.all()
    serializer= EmpleadoSerializer(empleados , many=True, context={'request' : request})
    return Response(serializer.data)

@api_view(['GET'])
def detalle_empleado(request,empleado_id):
    try:
        empleado=Empleado.objects.get(pk = empleado_id)
    except Empleado.DoesNotExist:
        return Response(
            {"razón": f"No existe un empleado asociado al id número {empleado_id}."},
            status = status.HTTP_404_NOT_FOUND
        )
    sin_detalle = ['id', 'nombre', 'apellido', 'legajo', 'activo']
    serializer= EmpleadoSerializer(empleado,
        fields = sin_detalle,
        context={'request' : request})
    return Response(serializer.data)