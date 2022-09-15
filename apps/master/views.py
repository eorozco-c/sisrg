from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.empresas.models import Empresa
from apps.usuarios.models import Usuario
from apps.estados.models import Nombre_estado
import psutil

# Create your views here.
def index(request):
    if request.method == "GET":
        if Nombre_estado.objects.count() == 0:
            Nombre_estado.objects.bulk_create([
                Nombre_estado(nombre='EN PROCESO', descripcion='Estado en el que se encuentra una solicitud en proceso de aprobación'),
                Nombre_estado(nombre='EN REVISION', descripcion='Estado en el que se encuentra una solicitud en proceso de revisión'),
                Nombre_estado(nombre='APROBADO', descripcion='Estado en el que se encuentra una solicitud aprobada'),
                Nombre_estado(nombre='RECHAZADO', descripcion='Estado en el que se encuentra una solicitud rechazada'),
                Nombre_estado(nombre='PAGADO', descripcion='Estado en el que se encuentra una solicitud pagada'),
                Nombre_estado(nombre='INICIADO', descripcion='Estado inicial de una solicitud'),
            ])
        if Empresa.objects.count() == 0:
            return redirect("empresas:crear")
        if Usuario.objects.count() == 0:
           return redirect("usuarios:registrar")
        if request.user.is_authenticated:
            return redirect("master:menu")
    return redirect("usuarios:login")
    
@login_required(login_url='/')
def menu(request):
    ramUsage = round(psutil.virtual_memory().percent)
    ramAvailable = round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    hdd = psutil.disk_usage('/')
    hddUsage = round(hdd.used / (2**30))
    hddAvailable = round(hdd.free / (2**30))
    usuarios = Usuario.objects.filter(empresa=request.user.empresa).count()
    context = {
        'appname' : "dashboard",
        'ramUsage' : ramUsage,
        'ramAvailable' : ramAvailable,
        'hddUsage' : hddUsage,
        'hddAvailable' : hddAvailable,
        'usuarios' : usuarios,
    }
    return render(request, "menu.html", context)