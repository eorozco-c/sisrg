from django.db import models
from apps.usuarios.models import Usuario
from apps.clientes.models import Cliente
#Sitios_cliente
from apps.estados.models import Nombre_estado

def file_path(instance, filename):
    return f'{instance.usuario.empresa.nombre}/rendiciones/{filename}'

# Create your models here.
class Rendicion(models.Model):
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="rendiciones_usuario")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="rendiciones_cliente")
    encargado = models.CharField(max_length=100,null=True,blank=True)
    sitios_cliente = models.CharField(max_length=255,blank=True,null=True)
    estado = models.ForeignKey(Nombre_estado, on_delete=models.PROTECT, related_name="rendiciones_nombre_estado")
    kilometraje_inicial = models.CharField(max_length=100,blank=True,null=True)
    kilometraje_final = models.CharField(max_length=100,blank=True,null=True)
    img_km_inicial = models.ImageField(upload_to=file_path, null=True, blank=True)
    img_km_final = models.ImageField(upload_to=file_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

def file_path_detalle(instance, filename):
    return f'{instance.rendicion.usuario.empresa.nombre}/rendiciones/{filename}'

class RendicionDetalle(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null=True)
    rendicion = models.ForeignKey(Rendicion, on_delete=models.PROTECT, related_name="rendiciones_detalle_rendicion")
    descripcion = models.TextField()
    monto_neto = models.CharField(max_length=100,blank=True,null=True)
    monto_iva = models.CharField(max_length=100,blank=True,null=True)
    imagen = models.ImageField(upload_to=file_path_detalle, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
