from django.urls import  path
from . import views

app_name = "rendiciones"

urlpatterns = [
    path('', views.ListaRendiciones.as_view(), name="index"),
    path('crear/', views.CrearRendicion.as_view(), name="crear"),
    path('editar/<int:pk>/', views.EditarRendicion.as_view(), name="editar"),
    path('predestroy/<int:pk>',views.predestroy,name='predestroy'),
    path('destroy/<int:pk>',views.destroy,name='destroy'),
    path('obtiene_sitios/<int:pk_cliente>', views.obtiene_sitios, name="obtiene_sitios"),
    path('detalle_rendicion/<int:pk>', views.DetalleRendicion.as_view(), name="detalle_rendicion"),
    path('detalle_rendicion/<int:pk_rendicion>/crear', views.CrearDetalleRendicion.as_view(), name="crear_detalle_rendicion"),
    path('detalle_rendicion/<int:pk_rendicion>/editar/<int:pk>', views.EditarDetalleRendicion.as_view(), name="editar_detalle_rendicion"),
    path('detalle_rendicion/<int:pk_rendicion>/predestroy/<int:pk>',views.predestroy_detalle,name='predestroy_detalle'),
    path('detalle_rendicion/<int:pk_rendicion>/destroy/<int:pk>',views.destroy_detalle,name='destroy_detalle'),
]