from django import forms
from .models import Viagem

class ViagemForm(forms.Form):
    class Meta:
        model = Viagem
        fields = ['destino', 'data_partida', 'preco']