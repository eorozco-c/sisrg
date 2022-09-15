from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'api'

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('sitios', SitioclienteViewSet)
router.register('estados', NombreEstadoViewSet)
router.register('rendiciones', RendicionViewSet)
router.register('detalle_rendicion/(?P<pk_rendicion>\\d+)', DetalleRendicionViewSet)

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('', include(router.urls)),
    path('validar-token/', ValidaToken.as_view(), name='validar-token'),
    path('detalle_rendicion/<int:pk_rendicion>/', DetalleRendicionViewSet.as_view({'get': 'list'}), name='detalle_rendicion'),
]