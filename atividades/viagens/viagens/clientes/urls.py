from django.urls import path
from .views import cadastrar_cliente, listar_clientes

urlpatterns = [
    path('listar_clientes/', listar_clientes, name='listar_clientes'),
    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
]
