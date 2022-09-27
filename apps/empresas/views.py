from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from apps.usuarios.models import Usuario
from .models import Empresa
from .formularios import FormularioEmpresa
import os
# Create your views here.

@method_decorator(login_required, name='dispatch')
class ListEmpresas(ListView):
    model = Empresa
    template_name = "empresas/empresas_list.html"

    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().get(*args, **kwargs)
        return redirect("master:index")

    def get_context_data(self, **kwargs):
        context = super(ListEmpresas, self).get_context_data(**kwargs)
        context['appname'] = "empresas" 
        return context

class CrearEmpresa(CreateView):
    template_name = "empresas/formulario.html"
    form_class = FormularioEmpresa
    success_url = reverse_lazy("empresas:index")

    def get_context_data(self, **kwargs):
        context = super(CrearEmpresa, self).get_context_data(**kwargs)
        context['legend'] = "Registro empresa"
        context['appname'] = "empresas"
        return context

    def get(self, *args, **kwargs):
        if self.request.user.is_superuser or Empresa.objects.count() == 0:
            return super().get(*args, **kwargs)
        return redirect("master:index")

    def form_valid(self,form):
        empresa = form.save()
        if not os.path.exists(f"media/{empresa.nombre}"):
            os.mkdir("media/"+empresa.nombre)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditEmpresa(UpdateView):
    template_name = "empresas/formulario.html"
    model = Empresa
    form_class = FormularioEmpresa
    success_url = reverse_lazy("empresas:index")

    def get_context_data(self, **kwargs):
        context = super(EditEmpresa, self).get_context_data(**kwargs)
        context['legend'] = "Editar Empresa"
        context['appname'] = "empresas"
        return context
        
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().get(*args, **kwargs)
        return redirect("master:index")

@login_required(login_url="/")
def predestroy(request, pk):
    if request.method == "GET":
        try:
            empresa = Empresa.objects.get(id=pk)
        except:
            return redirect("empresas:index")
        context={
            'id' : empresa.id,
            'nombre': empresa.nombre,
        }
        return JsonResponse(context)
    return redirect("empresas:index")

@login_required(login_url="/")
def destroy(request,pk):
    if request.method == "GET":
        if request.user.is_superuser:
            try:
                empresa = Empresa.objects.get(id=pk)
            except:
                return redirect("empresas:index")
            try:
                empresa.delete()
                #remove media folder
                if os.path.exists(f"media/{empresa.nombre}"):
                    os.rmdir("media/"+empresa.nombre)
            except:
                messages.success(request,f'No se puede eliminar empresa ya que tiene elementos asignados',extra_tags='danger')
                return redirect("empresas:index")
    return redirect("empresas:index")

@login_required(login_url="/")
def cambiarEmpresa(request, pk):
    if request.method == "GET":
        if request.user.is_superuser:
            empresa = Empresa.objects.get(id=pk)
            usuario = Usuario.objects.get(id=request.user.id)
            usuario.empresa = empresa
            usuario.save()
    return redirect("empresas:index")