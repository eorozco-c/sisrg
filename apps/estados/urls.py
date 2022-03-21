from django.urls import  path
from . import views

app_name = "estados"

urlpatterns = [
    path('', views.ListaEstados.as_view(), name="index"),
]