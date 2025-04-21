from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='clientes'),
    path('<int:cliente_id>/', views.cliente_detalhes, name='cliente_detalhes'),
]
