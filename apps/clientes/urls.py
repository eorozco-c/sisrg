from django.urls import  path
from . import views

app_name = "clientes"

urlpatterns = [
    path('', views.ListaClientes.as_view(), name="index"),
    path('crear', views.CrearClientes.as_view(), name="crear"),
    path('editar/<int:pk>', views.EditarCliente.as_view(), name="editar"),
    path('predestroy/<int:pk>',views.predestroy, name="predestroy"),
    path('destroy/<int:pk>',views.destroy, name="destroy"),
    path('sitios/<int:pk>', views.ListaSitiosCliente.as_view(), name="sitios"),
    path('sitios/crear/<int:pk>', views.CrearSitiosCliente.as_view(), name="sitios_crear"),
    path('sitios/editar/<int:pk>', views.EditarSitioCliente.as_view(), name="sitios_editar"),
    path('sitios/predestroy/<int:pk>/<int:pk_cliente>',views.predestroy_sitio, name="predestroy_sitio"),
    path('sitios/destroy/<int:pk>/<int:pk_cliente>',views.destroy_sitio, name="destroy_sitio"),
]