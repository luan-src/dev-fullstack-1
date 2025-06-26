from django.shortcuts import render, redirect
from .forms import ViagemForm
from .models import Viagem
from clientes.models import Cliente

def index(request):
    return render(request, 'viagens/index.html')

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
        'cliente': Cliente,
        'viagens': viagens_do_cliente
    }

    return render(request, 'viagens/viagem_por_clientes.html', context)