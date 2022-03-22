from dataclasses import field
import json
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages

from apps.clientes.models import Cliente, Sitios_cliente
from apps.estados.models import Nombre_estado
from apps.usuarios.models import Usuario
from .models import Rendicion
import datetime

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
        queryset = Rendicion.objects.filter(updated_at__range=[fecha_ini, fecha_fin],usuario__empresa=self.request.user.empresa)
        return queryset

@method_decorator(login_required, name='dispatch')
class CrearRendicion(CreateView):
    model = Rendicion
    template_name = 'rendiciones/formulario.html'
    fields = ['descripcion', 'usuario', 'cliente', 'encargado', 'sitios_cliente', 'estado']

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
            rendicion.sitios_cliente = Sitios_cliente.objects.get(id=self.request.POST.get('sitio'))
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
            sitios = cliente.sitios_cliente_cliente.all()
            return JsonResponse({"sitios":list(sitios.values())})
        except Cliente.DoesNotExist:
            return JsonResponse({"sitios": []})
    return JsonResponse({"sitios": []})

@method_decorator(login_required, name='dispatch')
class EditarRendicion(UpdateView):
    model = Rendicion
    template_name = 'rendiciones/formulario.html'
    fields = ['descripcion', 'usuario', 'cliente', 'encargado', 'sitios_cliente', 'estado']

    def get_context_data(self, **kwargs):
        context = super(EditarRendicion, self).get_context_data(**kwargs)
        context['legend'] = "Editar Rendición"
        context['appname'] = "rendiciones"
        context['clientes'] = Cliente.objects.filter(empresa=self.request.user.empresa)
        context['usuarios'] = Usuario.objects.filter(empresa=self.request.user.empresa, is_superuser=False)
        context['estados'] = Nombre_estado.objects.all()
        try:
            context['sitios'] = Sitios_cliente.objects.filter(cliente=self.object.cliente)
        except:
            context['sitios'] = []
        #data for prepopulate form in object
        data = json.dumps({
            'descripcion': self.object.descripcion,
            'usuario': self.object.usuario.id,
            'cliente': self.object.cliente.id,
            'encargado': self.object.encargado,
            'sitios_cliente': self.object.sitios_cliente.id,
            'estado': self.object.estado.id
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
            rendicion.sitios_cliente = Sitios_cliente.objects.get(id=self.request.POST.get('sitio'))
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
