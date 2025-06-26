from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from .forms import ClienteForm
from .models import Cliente

def index(request):
    return HttpResponse("Hello, world! This is the Clientes app index page.")

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