from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View
from .models import Servicio


# Views de listas

# Listar solo los activos
class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicios/listar_servicios.html'
    context_object_name = 'servicios'
    def get_queryset(self):
        return Servicio.objects.filter(activo=True)

# Listar inactivos
class ServicioInactivosListView(ListView):
    model = Servicio
    template_name = 'servicios/inactivos.html'
    context_object_name = 'servicios'

    def get_queryset(self):
        return Servicio.objects.filter(activo=False)


# Views de creación, edición, eliminación y restauración

#Creación
class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'servicios/form.html'
    fields = ['nombre', 'descripcion', 'precio']
    success_url = reverse_lazy('servicios:listar')

#Edición
class ServicioUpdateView(UpdateView):
    model = Servicio
    fields = ['nombre', 'descripcion', 'precio', 'activo']
    template_name = 'servicios/form.html'
    success_url = reverse_lazy('servicios:listar')

#Baja Lógica
class ServicioBajaLogicaView(View):
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.activo = False
        servicio.save()
        return redirect('servicios:listar')

#Restauración (active = False -> True)
class ServicioRestaurarView(View):
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.activo = True
        servicio.save()
        return redirect('servicios:inactivos')