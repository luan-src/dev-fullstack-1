from django import forms
from .models import Viagem

class ViagemForm(forms.ModelForm):
    data_partida = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )


    class Meta:
        model = Viagem
        fields = ['destino', 'data_partida', 'preco']