from django.shortcuts import render
from .models import Produto

# Create your views here.

def index(request):
    return render(request, 'produtos/index.html')

def produtos(request):
    #Obter todos os produtos do DB.
    produtos = Produto.objects.all()
    #É sempre necessário passar o conteúdo dentro de um dicionário, mesmo que seja apenas um único item.
    dados_produtos = {
        'produtos': produtos,
    }
    return render(request, 'produtos/produtos.html', dados_produtos)