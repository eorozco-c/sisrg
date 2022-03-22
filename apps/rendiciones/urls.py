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
]