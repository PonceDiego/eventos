from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View
from .models import Servicio, Cliente, Coordinador

# Landing Page
def home(request):
    return render(request, 'home.html')

# Views de listas

# Listar solo los activos
class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicios/listar_servicios.html'
    context_object_name = 'servicios'
    def get_queryset(self):
        return Servicio.objects.filter(activo=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_inactivo'] = False
        return context
    
class ClienteListView(ListView):
    model = Cliente
    template_name = 'servicios/lista_clientes.html'
    context_object_name = 'clientes'
    def get_queryset(self):
        return Cliente.objects.filter(activo=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_inactivo'] = False
        return context

class CoordinadorListView(ListView):
    model = Coordinador
    template_name = 'servicios/lista_coordinadores.html'
    context_object_name = 'coordinadores'
    def get_queryset(self):
        return Coordinador.objects.filter(activo = True)


# Listar inactivos
class ServicioInactivosListView(ListView):
    model = Servicio
    template_name = 'servicios/listar_servicios.html'
    context_object_name = 'servicios'

    def get_queryset(self):
        return Servicio.objects.filter(activo=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_inactivo'] = True
        return context

class ClienteInactivoListView(ListView):
    model = Cliente
    template_name = 'servicios/lista_clientes.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        return Cliente.objects.filter(activo=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_inactivo'] = True
        return context

class CoordinadorInactivoListView(ListView):
    model = Coordinador
    template_name = 'servicios/coordinadores_inactivos.html'
    context_object_name = 'coordinadores'

    def get_queryset(self):
        return Coordinador.objects.filter(activo=False)

# Views de creación, edición, eliminación y restauración cliente

#Creación
class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'servicios/form.html'
    fields = ['nombre', 'descripcion', 'precio']
    success_url = reverse_lazy('servicios:listar')

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'servicios/formcliente.html'
    fields = ['nombre' , 'apellido' , 'contacto']
    success_url = reverse_lazy('servicios:lista_cliente')

class CoordinadorCreateView(CreateView):
    model = Coordinador
    template_name = 'servicios/formCoordinadores.html'
    fields = ['nombre', 'apellido' ,'dni']
    success_url = reverse_lazy('servicios:lista_coordinador')

#Edición
class ServicioUpdateView(UpdateView):
    model = Servicio
    fields = ['nombre', 'descripcion', 'precio', 'activo']
    template_name = 'servicios/form.html'
    success_url = reverse_lazy('servicios:listar')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'servicios/formcliente.html'
    fields = ['nombre' , 'apellido' , 'contacto', 'activo']
    success_url = reverse_lazy('servicios:lista_cliente')

class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    template_name = 'servicios/formCoordinadores.html'
    fields = ['nombre', 'apellido' ,'dni' , 'fecha_alta']
    success_url = reverse_lazy('servicios:lista_coordinador')

#Baja Lógica
class ServicioBajaLogicaView(View):
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.activo = False
        servicio.save()
        return redirect('servicios:listar')

class ClienteBajaLogicaView(View):
    def post(self , request , pk):
        cliente = get_object_or_404(Cliente , pk = pk)
        cliente.activo = False
        cliente.save()
        return redirect('servicios:lista_cliente')

class CoordinadorBajaLogicaView(View):
    def post(self,request,pk):
        coordinador = get_object_or_404(Coordinador , pk=pk)
        coordinador.activo= False
        coordinador.save()
        return redirect('servicios:lista_coordinador')
    
#Restauración (active = False -> True)
class ServicioRestaurarView(View):
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.activo = True
        servicio.save()
        return redirect('servicios:inactivos')

class ClienteRestaurarView(View):
    def post(self , request , pk):
        cliente = get_object_or_404(Cliente , pk = pk)
        cliente.activo = True
        cliente.save()
        return redirect('servicios:cliente_inactivo')


class CoordinadorRestaurarView(View):
    def post(self , request , pk):
        coordinador = get_object_or_404(Coordinador , pk=pk)
        coordinador.activo=True
        coordinador.save()
        return redirect('servicios:coordinador_inactivo')

