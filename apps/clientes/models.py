from django.db import models
from apps.empresas.models import Empresa

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    logo = models.TextField(default="",blank=True,null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='clientes_empresa')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.nombre

# class Sitios_cliente(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='sitios_cliente_cliente')
#     nombre = models.CharField(max_length=100, unique=True)
#     direccion = models.CharField(max_length=100, blank=True, null=True)
#     telefono = models.CharField(max_length=100, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     encargado = models.CharField(max_length=100, blank=True, null=True)
#     empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='clientes_sitios_empresa')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__ (self):
#         return self.nombre