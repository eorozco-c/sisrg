from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_auth.models import TokenModel
from apps.clientes.models import Cliente, Sitios_cliente
from apps.estados.models import Nombre_estado
from apps.rendiciones.models import RendicionDetalle
from .serializers import *
# # Create your views here.

#create GET method that return true or false if the token is valid
class ValidaToken(APIView):
    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if token:
            token = token.replace('Token ', '')
            try:
                TokenModel.objects.get(key=token)
                return Response({"valid": True})
            except:
                return Response({"valid": False})
        else:
            return Response({"valid": False})
        
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

class NombreEstadoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Nombre_estado.objects.all()
    serializer_class = EstadosModelSerializer

class RendicionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Rendicion.objects.all()
    serializer_class = RendicionModelSerializer
    
    def get_queryset(self):
        queryset = Rendicion.objects.filter(usuario=self.request.user)
        return queryset

class DetalleRendicionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = RendicionDetalle.objects.all()
    serializer_class = RendicionDetalleModelSerializer

    def get_queryset(self):
        queryset = RendicionDetalle.objects.filter(rendicion_id=self.kwargs['pk_rendicion'])
        return queryset

    def perform_create(self, serializer):
        serializer.save(rendicion_id=self.kwargs['pk_rendicion'])