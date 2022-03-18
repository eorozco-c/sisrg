from ast import For
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Cliente, Sitios_cliente
from .formularios import FormularioCliente, FormularioSitioCliente

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ListaClientes(ListView):
    model = Cliente
    template_name = 'clientes/clientes_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListaClientes, self).get_context_data(**kwargs)
        context['appname'] = "clientes"
        return context

    def get_queryset(self):
        queryset = Cliente.objects.filter(empresa=self.request.user.empresa)
        return queryset
    
    def get(self, request):
        if self.request.user.has_perm('clientes.view_clientes'):
            return super().get(request)
        return redirect("master:index")

@method_decorator(login_required, name='dispatch')
class CrearClientes(CreateView):
    template_name = "clientes/formulario.html"
    form_class = FormularioCliente
    success_url = reverse_lazy("clientes:index")

    def form_valid(self, form):
        ruta = form.save(commit = False)
        ruta.empresa = self.request.user.empresa
        ruta.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearClientes, self).get_context_data(**kwargs)
        context['legend'] = "Agregar Cliente"
        context['appname'] = "clientes"
        return context

    def get(self, request):
        if self.request.user.has_perm('clientes.add_clientes'):
            return super().get(request)
        return redirect("master:index")

@method_decorator(login_required, name='dispatch')
class EditarCliente(UpdateView):
    template_name = "clientes/formulario.html"
    model = Cliente
    form_class = FormularioCliente
    success_url = reverse_lazy("clientes:index")

    def get_context_data(self, **kwargs):
        context = super(EditarCliente, self).get_context_data(**kwargs)
        context['legend'] = "Editar Cliente"
        context['appname'] = "clientes"
        return context

    def get(self, request, pk):
        objeto = self.get_object()
        if self.request.user.empresa != objeto.empresa:
            return redirect("master:index")
        elif not self.request.user.has_perm('clientes.change_clientes'):
            return redirect("clientes:index")
        return super().get(request)

@login_required(login_url="/")
def predestroy(request, pk):
    if request.user.has_perm('clientes.delete_clientes'):
        if request.method == "GET":
            try:
                cliente = Cliente.objects.get(id=pk)
            except:
                return redirect("clientes:index")
            context={
                'nombre' : cliente.nombre,
                'direccion': cliente.direccion,
                'id': cliente.id,
            }
            return JsonResponse(context)
    return redirect("clientes:index")


@login_required(login_url="/")
def destroy(request,pk):
    if request.user.has_perm('clientes.delete_clientes'):
        if request.method == "GET":
            try:
                cliente = Cliente.objects.get(id=pk)
            except:
                return redirect("clientes:index")
            if request.user.empresa == cliente.empresa:
                try:
                    cliente.delete()
                except:
                    messages.success(request,f'No se puede eliminar elemento',extra_tags='danger')
    return redirect("clientes:index")


@method_decorator(login_required, name='dispatch')
class ListaSitiosCliente(ListView):
    model = Sitios_cliente
    template_name = 'clientes/sitios_list.html'

    def get_context_data(self, **kwargs):
        context = super(ListaSitiosCliente, self).get_context_data(**kwargs)
        try:
            cliente = Cliente.objects.get(id=self.kwargs['pk'])
        except:
            messages.success(self.request,f'Cliente no existe',extra_tags='danger')
            return redirect("clientes:sitios", pk=self.kwargs['pk'])
        context['appname'] = "sitios"
        context['id_cliente'] = cliente.id
        context['nombre_cliente'] = cliente.nombre
        context['object_list'] = Sitios_cliente.objects.filter(empresa=self.request.user.empresa,cliente=cliente)
        return context

    def get_queryset(self):
        queryset = Sitios_cliente.objects.filter(empresa=self.request.user.empresa)
        return queryset
    
    def get(self, request,pk):
        if self.request.user.has_perm('clientes.view_sitios_cliente'):
            return super().get(request)
        return redirect("master:index")

@method_decorator(login_required, name='dispatch')
class CrearSitiosCliente(CreateView):
    template_name = "clientes/formulario.html"
    form_class = FormularioSitioCliente

    def form_valid(self, form):
        ruta = form.save(commit = False)
        try:
            cliente = Cliente.objects.get(id=self.kwargs['pk'])
        except:
            messages.success(self.request,f'Error al crear sitio',extra_tags='danger')
            return redirect("clientes:sitios", pk=self.kwargs['pk'])
        ruta.cliente = cliente
        ruta.empresa = self.request.user.empresa
        ruta.save()
        return redirect("clientes:sitios", pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(CrearSitiosCliente, self).get_context_data(**kwargs)
        try:
            cliente = Cliente.objects.get(id=self.kwargs['pk'])
        except:
            messages.success(self.request,f'Error al crear sitio',extra_tags='danger')
            return redirect("clientes:sitios", pk=self.kwargs['pk'])
        context['legend'] = f"Agregar Sitio a {cliente.nombre.capitalize()}"
        context['appname'] = "sitios"
        return context

    def get(self, request,pk):
        if self.request.user.has_perm('clientes.add_sitios_cliente'):
            return super().get(request)
        return redirect("master:index")

@method_decorator(login_required, name='dispatch')
class EditarSitioCliente(UpdateView):
    template_name = "clientes/formulario.html"
    model = Sitios_cliente
    form_class = FormularioSitioCliente

    def form_valid(self,form):
        form.save()
        return redirect("clientes:sitios", pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(EditarSitioCliente, self).get_context_data(**kwargs)
        context['legend'] = "Editar Sitio"
        context['appname'] = "sitios"
        return context

    def get(self, request,pk):
        objeto = self.get_object()
        if self.request.user.empresa != objeto.empresa:
            return redirect("master:index")
        elif not self.request.user.has_perm('clientes.change_sitios_cliente'):
            return redirect("clientes:sitios", pk=self.kwargs['pk'])
        return super().get(request)

@login_required(login_url="/")
def predestroy_sitio(request, pk,pk_cliente):
    if request.user.has_perm('clientes.delete_sitios_cliente'):
        if request.method == "GET":
            try:
                sitio = Sitios_cliente.objects.get(id=pk)
            except:
                return redirect("clientes:sitios", pk=pk_cliente)
            context={
                'nombre' : sitio.nombre,
                'direccion': sitio.direccion,
                'encargado': sitio.encargado,
                'id': sitio.id,
            }
            return JsonResponse(context)
    return redirect("clientes:sitios", pk=pk_cliente)

@login_required(login_url="/")
def destroy_sitio(request, pk,pk_cliente):
    if request.user.has_perm('clientes.delete_sitios_cliente'):
        if request.method == "GET":
            try:
                sitio = Sitios_cliente.objects.get(id=pk)
            except:
                return redirect("clientes:sitios", pk=pk_cliente)
            if request.user.empresa == sitio.empresa:
                try:
                    sitio.delete()
                except:
                    messages.success(request,f'No se puede eliminar elemento',extra_tags='danger')
    return redirect("clientes:sitios", pk=pk_cliente)