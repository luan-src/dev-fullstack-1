from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            input_formats=['%Y-%m-%d']
        )

    class Meta:
        model = Cliente
        fields = ['nome', 'email',  'data_nascimento', 'cpf']

