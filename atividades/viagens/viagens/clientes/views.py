from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ClienteForm
from .models import Cliente
from viagens.forms import ViagemForm
from viagens.models import Viagem

def index(request):
    return render(request, 'index.html')


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
        dados = {'form': form}
    return render(request, 'clientes/cadastrar_clientes.html', dados)

def listar_clientes(request):
    clientes = Cliente.objects.all()
    dados = {'clientes': clientes}
    return render(request, 'clientes/listar_clientes.html', dados)

def nova_viagem(request):
    if request.method == 'POST':
        form = ViagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_viagens')
    else:
        form = ViagemForm()
        dados = {'form': form}
    return render(request, 'viagens/nova_viagem.html', dados)

def listar_viagens(request):
    viagens = Viagem.objects.all()
    dados = {'viagens': viagens}
    return render(request, 'viagens/listar_viagens.html', dados)

def cliente_viagens(request, cliente_id):
    viagens_do_cliente = Cliente.objects.get(pk=cliente_id).viagens.all()

    context = {
        'viagens': viagens_do_cliente
    }

    return render(request, 'viagens/viagem_por_clientes.html', context)
