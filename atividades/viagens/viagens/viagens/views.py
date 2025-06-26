from django.shortcuts import render, HttpResponse, redirect
from .forms import ViagemForm
from .models import Viagem

def index(request):
    return HttpResponse("Hello, world! This is the Viagens app index page.")


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