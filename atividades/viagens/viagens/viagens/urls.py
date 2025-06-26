from django.urls import path
from .views import listar_viagens, nova_viagem, cliente_viagens, index

urlpatterns = [
    path('', index, name='index'),
    path('listar_viagens/', listar_viagens, name='listar_viagens'),
    path('nova_viagem/', nova_viagem, name='nova_viagem'),
    path('clientes/<int:cliente_id>/viagens/', cliente_viagens, name='cliente_viagens'),
]
