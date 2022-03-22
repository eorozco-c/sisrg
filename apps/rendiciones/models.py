from django.db import models
from apps.usuarios.models import Usuario
from apps.clientes.models import Cliente, Sitios_cliente
from apps.estados.models import Nombre_estado

# Create your models here.
class Rendicion(models.Model):
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="rendiciones_usuario")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="rendiciones_cliente")
    encargado = models.CharField(max_length=100)
    sitios_cliente = models.ForeignKey(Sitios_cliente, on_delete=models.PROTECT, related_name="rendiciones_sitios_cliente")
    estado = models.ForeignKey(Nombre_estado, on_delete=models.PROTECT, related_name="rendiciones_nombre_estado")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id