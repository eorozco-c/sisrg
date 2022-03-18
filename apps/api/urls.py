from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet

app_name = 'api'

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('', include(router.urls)),
]