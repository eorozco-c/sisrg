from urllib import request
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets, permissions

from apps.clientes.models import Cliente, Sitios_cliente
from .serializers import ClienteModelSerializer, Sitios_clienteModelSerializer
# # Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteModelSerializer

    def get_queryset(self):
        queryset = Cliente.objects.filter(empresa=self.request.user.empresa)
        return queryset

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user.empresa)

class SitioclienteViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Sitios_cliente.objects.all()
    serializer_class = Sitios_clienteModelSerializer

    def get_queryset(self):
        queryset = Sitios_cliente.objects.filter(empresa=self.request.user.empresa)
        return queryset

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user.empresa)