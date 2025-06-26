from django.urls import path
from .views import cadastrar_cliente, listar_clientes, index, cliente_viagens, listar_viagens, nova_viagem

urlpatterns = [
    path('', index, name='index'),
    path('listar_clientes/', listar_clientes, name='listar_clientes'),
    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_viagens/', listar_viagens, name='listar_viagens'),
    path('nova_viagem/', nova_viagem, name='nova_viagem'),
    path('clientes/<int:cliente_id>/viagens/', cliente_viagens, name='cliente_viagens'),
]
