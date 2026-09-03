import os
import django
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyApp.settings')
django.setup()

from servicios.models import Cliente, Servicio, Empleado, Coordinador, Cliente, ReservaServicios
from datetime import timedelta
from django.utils import timezone

print("Limpiando datos antiguos...")
ReservaServicios.objects.all().delete()
Servicio.objects.all().delete()
Cliente.objects.all().delete()
Empleado.objects.all().delete()
Coordinador.objects.all().delete()

# 1. Crear 10 Servicios temáticos
servicios_datos = [
    ("Fiesta de 15 Años", "Organización integral para quinceañeras, incluye DJ e iluminación.", 1200000.00),
    ("Casamiento", "Planificación de boda con ambientación, catering premium y fotografía.", 2500000.00),
    ("Evento Corporativo", "Coordinación para conferencias, lanzamientos de productos y jornadas.", 950000.00),
    ("Cumpleaños Infantil", "Animación temática, inflables y mesa dulce para niños.", 350000.00),
    ("Aniversario de Bodas", "Cena show exclusiva con decoración elegante e iluminación tenue.", 600000.00),
    ("Fiesta de Egresados", "Producción para promociones escolares con pista LED y recepción.", 1800000.00),
    ("Catering Exclusivo", "Servicio gastronómico formal de 4 pasos con maridaje de vinos.", 800000.00),
    ("Bar / Bat Mitzvá", "Celebración tradicional con DJ, escenario y coordinación total.", 1400000.00),
    ("Coctelería y Barra Móvil", "Servicio de coctelería de autor con bartenders profesionales.", 450000.00),
    ("Show en Vivo y DJ Set", "Estructura de sonido profesional, luces robóticas y DJ residente.", 500000.00),
]

servicios_objs = [Servicio(nombre=nom, descripcion=desc, precio=prec) for nom, desc, prec in servicios_datos]
Servicio.objects.bulk_create(servicios_objs)

NOMBRES = [
    "Lucas", "Mateo", "Sofía", "Valentina", "Joaquín", "Camila", "Benjamín", "Martina", 
    "Santiago", "Lucía", "Nicolás", "Elena", "Tomás", "Mariana", "Agustín", "Paula",
    "Ignacio", "Daniela", "Facundo", "Victoria", "Gonzalo", "Renata", "Manuel", "Carolina"
]

APELLIDOS = [
    "González", "Rodríguez", "Gómez", "Fernández", "López", "Díaz", "Martínez", "Pérez",
    "García", "Sánchez", "Romero", "Sosa", "Torres", "Álvarez", "Ruiz", "Ramírez",
    "Flores", "Benítez", "Acosta", "Medina", "Herrera", "Castro", "Molina", "Ortiz"
]

empleados = [
    Empleado(
        nombre=random.choice(NOMBRES),
        apellido=random.choice(APELLIDOS),
        legajo=1000 + i
    )
    for i in range(1, 51)
]
Empleado.objects.bulk_create(empleados)

coordinadores = [
    Coordinador(
        nombre=random.choice(NOMBRES),
        apellido=random.choice(APELLIDOS),
        dni=str(random.randint(28000000, 45000000))
    )
    for _ in range(15)
]
Coordinador.objects.bulk_create(coordinadores)

DOMINIOS = ["gmail.com", "outlook.com", "yahoo.com", "events.com", "hotmail.com"]

clientes_a_crear = []

for i in range(1, 51):
    nombre = random.choice(NOMBRES)
    apellido = random.choice(APELLIDOS)
    # Formato de contacto: a@a.com, nombre.apellidoXX@dominio.com o variaciones simples
    contacto = f"{nombre.lower()}.{apellido.lower()}{i}@{random.choice(DOMINIOS)}"
    
    clientes_a_crear.append(
        Cliente(
            nombre=nombre,
            apellido=apellido,
            contacto=contacto
        )
    )

Cliente.objects.bulk_create(clientes_a_crear)


print("Insertando Reservas...")
clientes = list(Cliente.objects.all())
servicios = list(Servicio.objects.all())
empleados = list(Empleado.objects.all())
coordinadores = list(Coordinador.objects.all())

if clientes:
    reservas_objs = []
    fecha_base = timezone.now()

    for servicio in servicios:
        fecha_evento = fecha_base + timedelta(days=random.randint(1, 60), hours=random.randint(10, 22))
        reservas_objs.append(
            ReservaServicios(
                cliente=random.choice(clientes),
                servicio=servicio,
                empleado=random.choice(empleados),
                coordinador=random.choice(coordinadores),
                fecha_servicio=fecha_evento
            )
        )
    ReservaServicios.objects.bulk_create(reservas_objs)
    print("¡Población completada con éxito sin duplicados!")
else:
    print("Atención: No hay clientes cargados. Cargá clientes primero para generar las reservas.")
    print("¡Base de datos cargada exitosamente!")