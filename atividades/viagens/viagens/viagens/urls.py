from django.urls import path
from .views import listar_viagens, nova_viagem

urlpatterns = [
    path('', listar_viagens, name='listar_viagens'),
    path('nova_viagem/', nova_viagem, name='nova_viagem'),
]
