from rest_framework import serializers
from apps.clientes.models import Cliente, Sitios_cliente
from rest_framework.authtoken.models import Token


class ClienteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ('empresa','logo')

class Sitios_clienteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitios_cliente
        exclude = ('empresa',)