from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'api'

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
# router.register('sitios', SitioclienteViewSet)
router.register('estados', NombreEstadoViewSet)
router.register('rendiciones', RendicionViewSet)
router.register('rendiciones_estado/(?P<pk_estado>\d+)', RendicionesEstadoViewSet)
router.register('detalle_rendicion/(?P<pk_rendicion>\d+)', DetalleRendicionViewSet)
router.register('tipo_de_gastos', TipoDeGastoViewSet)


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('', include(router.urls)),
    path('validar-token/', ValidaToken.as_view(), name='validar-token'),
]