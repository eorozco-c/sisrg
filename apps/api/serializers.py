from dataclasses import field
from rest_framework import serializers
from apps.clientes.models import Cliente, Sitios_cliente
from apps.usuarios.models import Usuario
from apps.estados.models import Nombre_estado
from django.conf import settings
from rest_auth.models import TokenModel
from rest_auth.utils import import_callable
from rest_auth.serializers import UserDetailsSerializer as DefaultUserDetailsSerializer

rest_auth_serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})
UserDetailsSerializer = import_callable(
    rest_auth_serializers.get('USER_DETAILS_SERIALIZER', DefaultUserDetailsSerializer)
)

class UserDetailsSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = TokenModel
        fields = ('key', 'user', )

class ClienteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ('empresa','logo')

class Sitios_clienteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitios_cliente
        exclude = ('empresa',)

class EstadosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nombre_estado
        fields = ("__all__")