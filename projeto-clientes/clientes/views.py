from django.shortcuts import render, get_object_or_404
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def cliente_detalhes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id) #chatgpt recomendou botar isso aqui
    return render(request, 'clientes/clientes-completos.html', {'cliente': cliente})
