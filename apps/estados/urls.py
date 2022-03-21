from django.urls import  path
from . import views

app_name = "estados"

urlpatterns = [
    path('', views.ListaEstados.as_view(), name="index"),
    # path('crear', views.CrearClientes.as_view(), name="crear"),
    # path('editar/<int:pk>', views.EditarCliente.as_view(), name="editar"),
    # path('predestroy/<int:pk>',views.predestroy, name="predestroy"),
    # path('destroy/<int:pk>',views.destroy, name="destroy"),
]