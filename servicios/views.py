from django.forms.widgets import DateTimeInput
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from .models import Servicio, Cliente, Coordinador , Empleado, ReservaServicios

# Landing Page
def home(request):
    servicios = Servicio.objects.filter(activo=True)
    return render(request, 'home.html', {'servicios' : servicios})

# Views de listas

# Listar solo los activos
class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicios/lista_servicios.html'
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_inactivo'] = False
        return context

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'servicios/lista_empleados.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        return Empleado.objects.filter(activo=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_inactivo'] = False
        return context


# Listar inactivos
class ServicioInactivosListView(ListView):
    model = Servicio
    template_name = 'servicios/lista_servicios.html'
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
    template_name = 'servicios/lista_coordinadores.html'
    context_object_name = 'coordinadores'

    def get_queryset(self):
        return Coordinador.objects.filter(activo=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_inactivo'] = True
        return context

class EmpleadoInactivoListView(ListView):
    model = Coordinador
    template_name = 'servicios/lista_empleados.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        return Empleado.objects.filter(activo=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_inactivo'] = True
        return context

class ReservaListView(ListView):
    model = ReservaServicios
    template_name = 'servicios/lista_reservas.html'
    context_object_name = 'reservas'

# Views de creación, edición, eliminación y restauración cliente

#Creación
class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'servicios/form.html'
    fields = ['nombre', 'descripcion', 'precio']
    success_url = reverse_lazy('servicios:listar')

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'servicios/form_cliente.html'
    fields = ['nombre' , 'apellido' , 'contacto']
    success_url = reverse_lazy('servicios:lista_cliente')

class CoordinadorCreateView(CreateView):
    model = Coordinador
    template_name = 'servicios/formCoordinadores.html'
    fields = ['nombre', 'apellido' ,'dni']
    success_url = reverse_lazy('servicios:lista_coordinador')

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'servicios/formEmpleados.html'
    fields = ['nombre' , 'apellido' , 'legajo']
    success_url = reverse_lazy('servicios:lista_empleados')

class ReservaCreateView(CreateView):
    model = ReservaServicios
    template_name = 'servicios/form_reserva.html'
    success_url = reverse_lazy('servicios:lista_reservas')
    fields = ['cliente', 'servicio', 'empleado', 'coordinador', 'fecha_servicio']

    def get_initial(self):
        initial = super().get_initial()
        servicio_id = self.request.GET.get('servicio_id')
        if servicio_id:
            initial['servicio'] = servicio_id
        return initial

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        return custom_form(form)
    
def custom_form(form):
    form.fields['fecha_servicio'].widget = DateTimeInput(
        attrs={
            'type' : 'datetime-local',
            'class' : 'form-control'
        }
    )

    select_fields = {
        'cliente' : 'Seleccione un Cliente',
        'servicio' : 'Seleccione un Servicio',
        'empleado' : 'Selecciones un Empleado',
        'coordinador' : 'Seleccione un Coordinador',
    }
    for field, placeholder in select_fields.items():
        form.fields[field].widget.attrs.update({'class' : 'form-select'})
        form.fields[field].empty_label = f"- {placeholder} -"

    # Filtrar solo activos
    form.fields['cliente'].queryset = Cliente.objects.filter(activo=True)
    form.fields['servicio'].queryset = Servicio.objects.filter(activo=True)
    form.fields['empleado'].queryset = Empleado.objects.filter(activo=True)
    form.fields['coordinador'].queryset = Coordinador.objects.filter(activo=True)

    return form

#Edición

class ServicioUpdateView(UpdateView):
    model = Servicio
    fields = ['nombre', 'descripcion', 'precio', 'activo']
    template_name = 'servicios/form.html'
    success_url = reverse_lazy('servicios:listar')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'servicios/form_cliente.html'
    fields = ['nombre' , 'apellido' , 'contacto', 'activo']
    success_url = reverse_lazy('servicios:lista_cliente')

class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    template_name = 'servicios/formCoordinadores.html'
    fields = ['nombre', 'apellido' ,'dni', 'activo']
    success_url = reverse_lazy('servicios:lista_coordinador')

class EmpleadoUpdateView(UpdateView):
    model= Empleado
    template_name = 'servicios/formEmpleados.html'
    fields = ['nombre' , 'apellido' , 'legajo', 'activo']
    success_url = reverse_lazy('servicios:lista_empleados')

class ReservaUpdateView(UpdateView):
    model = ReservaServicios
    template_name = 'servicios/form_reserva.html'
    success_url = reverse_lazy('servicios:lista_reservas')
    fields = ['cliente', 'servicio', 'empleado', 'coordinador', 'fecha_servicio']

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        return custom_form(form)

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

class EmpleadoBajaLogicaView(View):
    def post(self,request,pk):
        empleado = get_object_or_404(Empleado , pk=pk)
        empleado.activo= False
        empleado.save()
        return redirect('servicios:lista_empleados')
    
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

class EmpleadoRestaurarView(View):
    def post(self , request , pk):
        empleado = get_object_or_404(Empleado , pk=pk)
        empleado.activo=True
        empleado.save()
        return redirect('servicios:empleado_inactivo')

# Baja real
class ReservaDeleteView(DeleteView):
    model = ReservaServicios
    template_name = 'servicios/reserva_confirmar.html'
    success_url = reverse_lazy('servicios:lista_reservas')