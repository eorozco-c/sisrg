from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse_lazy
from apps.clientes.models import Cliente
#, Sitios_cliente
from apps.estados.models import Nombre_estado
from apps.usuarios.models import Usuario
from .models import *
from .formularios import RendicionDetalleForm, FormularioTipoDeGasto
import datetime, os, json

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ListaRendiciones(ListView):
    model = Rendicion
    template_name = 'rendiciones/rendiciones_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListaRendiciones, self).get_context_data(**kwargs)
        context['appname'] = "rendiciones"
        #from get data set fecha_ini and fecha_fin
        context['fecha_ini'] = self.request.GET.get('fecha_ini')
        context['fecha_fin'] = self.request.GET.get('fecha_fin')
        return context
    
    def get(self, request):
        if self.request.user.has_perm('rendiciones.view_rendiciones'):
            return super().get(request)
        return redirect("master:index")

    def get_queryset(self):
        fecha_ini = self.request.GET.get('fecha_ini')
        fecha_fin = self.request.GET.get('fecha_fin')
        if not fecha_ini or not fecha_fin:
            fecha_ini = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            fecha_fin = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)        
        queryset = Rendicion.objects.filter(updated_at__range=[fecha_ini, fecha_fin],usuario__empresa=self.request.user.empresa).exclude(estado__nombre="INICIADO")
        return queryset

@method_decorator(login_required, name='dispatch')
class CrearRendicion(CreateView):
    model = Rendicion
    template_name = 'rendiciones/formulario.html'
    fields = ['descripcion', 'usuario', 'cliente', 'encargado', 'estado']

    def get_context_data(self, **kwargs):
        context = super(CrearRendicion, self).get_context_data(**kwargs)
        context['legend'] = "Crear Rendición"
        context['appname'] = "rendiciones"
        context['clientes'] = Cliente.objects.filter(empresa=self.request.user.empresa)
        context['usuarios'] = Usuario.objects.filter(empresa=self.request.user.empresa, is_superuser=False)
        context['estados'] = Nombre_estado.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if request.user.has_perm('rendiciones.add_rendicion'):
            rendicion = Rendicion()
            rendicion.descripcion = self.request.POST.get('descripcion')
            rendicion.usuario = Usuario.objects.get(id=self.request.POST.get('usuario'))
            rendicion.cliente = Cliente.objects.get(id=self.request.POST.get('cliente'))
            rendicion.encargado = self.request.POST.get('encargado')
            rendicion.estado = Nombre_estado.objects.get(id=self.request.POST.get('estado'))
            rendicion.save()
            messages.success(self.request, 'Rendición creada correctamente')
            return redirect('rendiciones:index')
        return redirect("master:index")

@login_required(login_url="/")
def obtiene_sitios(request, pk_cliente):
    if request.method == "GET":
        if pk_cliente == "0":
            return JsonResponse({"sitios": []})
        try:
            cliente = Cliente.objects.get(pk=pk_cliente)
            # sitios = cliente.sitios_cliente_cliente.all()
            return JsonResponse({"sitios":list(sitios.values())})
        except Cliente.DoesNotExist:
            return JsonResponse({"sitios": []})
    return JsonResponse({"sitios": []})

@method_decorator(login_required, name='dispatch')
class EditarRendicion(UpdateView):
    model = Rendicion
    template_name = 'rendiciones/formulario.html'
    fields = ['descripcion', 'usuario', 'cliente', 'encargado','estado']

    def get_context_data(self, **kwargs):
        context = super(EditarRendicion, self).get_context_data(**kwargs)
        context['legend'] = "Editar Rendición"
        context['appname'] = "rendiciones"
        context['clientes'] = Cliente.objects.filter(empresa=self.request.user.empresa)
        context['usuarios'] = Usuario.objects.filter(empresa=self.request.user.empresa, is_superuser=False)
        context['estados'] = Nombre_estado.objects.all()
        #data for prepopulate form in object
        data = json.dumps({
            'descripcion': self.object.descripcion,
            'usuario': self.object.usuario.id,
            'cliente': self.object.cliente.id,
            'encargado': self.object.encargado,
            'estado': self.object.estado.id,

        })
        context['data'] = data
        return context

    def post(self, request, *args, **kwargs):
        if request.user.has_perm('rendiciones.change_rendicion'):
            rendicion = Rendicion.objects.get(pk=self.kwargs['pk'])
            rendicion.descripcion = self.request.POST.get('descripcion')
            rendicion.usuario = Usuario.objects.get(id=self.request.POST.get('usuario'))
            rendicion.cliente = Cliente.objects.get(id=self.request.POST.get('cliente'))
            rendicion.encargado = self.request.POST.get('encargado')
            rendicion.estado = Nombre_estado.objects.get(id=self.request.POST.get('estado'))
            rendicion.save()
            messages.success(self.request, 'Rendición editada correctamente')
            return redirect('rendiciones:index')
        return redirect("master:index")

@login_required(login_url="/")
def predestroy(request, pk):
    if request.method == "GET":
        try:
            rendicion = Rendicion.objects.get(pk=pk)
        except:
            return redirect("rendiciones:index")
        context={
            'id' : rendicion.id,
            'descripcion': rendicion.descripcion,
            'usuario' : rendicion.usuario.first_name + " " + rendicion.usuario.last_name,
        }
        return JsonResponse(context)
    return redirect("rendiciones:index")

@login_required(login_url="/")
def destroy(request,pk):
    if request.method == "GET":
        if request.user.is_superuser:
            try:
                rendicion = Rendicion.objects.get(pk=pk)
            except:
                return redirect("rendiciones:index")
            if request.user.empresa != rendicion.usuario.empresa:
                return redirect("master:index")
            rendicion.delete()
        else:
            messages.error(request, 'No tiene permisos para eliminar rendiciones')
    return redirect("rendiciones:index")


@method_decorator(login_required, name='dispatch')
class DetalleRendicion(ListView):
    model = RendicionDetalle
    template_name = 'rendiciones/detalle_list.html'
    context_object_name = 'rendicion'
    
    def get(self, request, pk):
        if self.request.user.has_perm('rendiciones.add_rendiciondetalle'):
            return super().get(request)
        return redirect("rendiciones:detalle_rendicion", pk=pk)

    #filter queryset
    def get_queryset(self):
        return RendicionDetalle.objects.filter(rendicion=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(DetalleRendicion, self).get_context_data(**kwargs)
        context['appname'] = "rendiciones_detalle"
        context['pk'] = self.kwargs['pk']
        return context
        
@method_decorator(login_required, name='dispatch')
class CrearDetalleRendicion(CreateView):
    form_class = RendicionDetalleForm
    template_name = 'formularios/generico.html'
    success_url: reverse_lazy('rendiciones:index')

    def get_context_data(self, **kwargs):
        context = super(CrearDetalleRendicion, self).get_context_data(**kwargs)
        context['legend'] = "Crear Detalle de Rendición"
        context['appname'] = "rendiciones"
        context['pk'] = self.kwargs['pk_rendicion']
        return context

    def form_valid(self, form):
        if self.request.user.has_perm('rendiciones.add_rendiciondetalle'):
            form.instance.rendicion = Rendicion.objects.get(pk=self.kwargs['pk_rendicion'])
            form.instance.save()
            messages.success(self.request, 'Detalle de rendición creado correctamente')
            return redirect('rendiciones:detalle_rendicion', pk=self.kwargs['pk_rendicion'])
        return redirect("rendiciones:detalle_rendicion", pk=self.kwargs['pk_rendicion'])


@method_decorator(login_required, name='dispatch')
class EditarDetalleRendicion(UpdateView):
    template_name = 'formularios/generico.html'
    model = RendicionDetalle
    form_class = RendicionDetalleForm

    def get_context_data(self, **kwargs):
        context = super(EditarDetalleRendicion, self).get_context_data(**kwargs)
        context['legend'] = "Editar Detalle de Rendición"
        context['appname'] = "rendiciones"
        return context

    def form_valid(self, form):
        form.save()
        return redirect("rendiciones:detalle_rendicion", pk=self.kwargs['pk_rendicion'])

@login_required(login_url="/")
def predestroy_detalle(request, pk_rendicion, pk):
    if request.method == "GET":
        try:
            detalle = RendicionDetalle.objects.get(pk=pk)
        except:
            return redirect("rendiciones:index")
        context={
            'rendicion_id' : pk_rendicion,
            'id' : detalle.id,
            'nombre': detalle.nombre,
            'descripcion': detalle.descripcion,
        }
        return JsonResponse(context)
    return redirect("rendiciones:detalle_rendicion", pk=pk_rendicion)

@login_required(login_url="/")
def destroy_detalle(request,pk_rendicion,pk):
    if request.method == "GET":
        if request.user.is_superuser:
            try:
                detalle = RendicionDetalle.objects.get(pk=pk)
            except:
                return redirect("rendiciones:detalle_rendicion", pk=pk_rendicion)
            detalle.delete()
        else:
            messages.error(request, 'No tiene permisos para eliminar rendiciones')
    return redirect("rendiciones:detalle_rendicion", pk=pk_rendicion)

@method_decorator(login_required, name='dispatch')
class ListTipoDeGasto(ListView):
    model = TipoDeGasto
    template_name = 'rendiciones/tipo_de_gasto_list.html'
    context_object_name = 'tipos_de_gasto'
    
    def get(self, request):
        if self.request.user.has_perm('rendiciones.view_tipodegasto'):
            return super().get(request)
        return redirect("master:index")

    def get_context_data(self, **kwargs):
        context = super(ListTipoDeGasto, self).get_context_data(**kwargs)
        context['appname'] = "tipos_de_gasto"
        return context

@method_decorator(login_required, name='dispatch')
class CrearTipoDeGasto(CreateView):
    form_class = FormularioTipoDeGasto
    template_name = 'formularios/generico.html'
    success_url: reverse_lazy('rendiciones:tipo_de_gasto')

    def get_context_data(self, **kwargs):
        context = super(CrearTipoDeGasto, self).get_context_data(**kwargs)
        context['legend'] = "Crear Tipo de Gasto"
        context['appname'] = "tipo_de_gasto"
        return context

    def form_valid(self, form):
        if self.request.user.has_perm('rendiciones.add_tipodegasto'):
            form.save()
            messages.success(self.request, 'Tipo de gasto creado correctamente')
            return redirect('rendiciones:tipo_de_gasto')
        return redirect("rendiciones:tipo_de_gasto")


@method_decorator(login_required, name='dispatch')
class EditarTipoDeGasto(UpdateView):
    template_name = 'formularios/generico.html'
    model = TipoDeGasto
    form_class = FormularioTipoDeGasto

    def get_context_data(self, **kwargs):
        context = super(EditarTipoDeGasto, self).get_context_data(**kwargs)
        context['legend'] = "Editar Tipo de Gasto"
        context['appname'] = "tipo_de_gasto"
        return context

    def form_valid(self, form):
        form.save()
        return redirect("rendiciones:tipo_de_gasto")

@login_required(login_url="/")
def predestroy_tipo_de_gasto(request, pk):
    if request.method == "GET":
        try:
            tipo_de_gasto = TipoDeGasto.objects.get(pk=pk)
        except:
            return redirect("rendiciones:tipo_de_gasto")
        context={
            'id' : tipo_de_gasto.id,
            'nombre': tipo_de_gasto.nombre,
            'descripcion': tipo_de_gasto.descripcion,
        }
        return JsonResponse(context)
    return redirect("rendiciones:tipo_de_gasto")


@login_required(login_url="/")
def destroy_tipo_de_gasto(request,pk):
    if request.method == "GET":
        if request.user.is_superuser:
            try:
                tipo_de_gasto = TipoDeGasto.objects.get(pk=pk)
            except:
                return redirect("rendiciones:tipo_de_gasto")
            tipo_de_gasto.delete()
        else:
            messages.error(request, 'No tiene permisos para eliminar tipos de gasto')
    return redirect("rendiciones:tipo_de_gasto")