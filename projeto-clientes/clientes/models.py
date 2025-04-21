from django.db import models

class Cliente(models.Model):

    COMPLEMENTOS = [
        ('CASA', 'Casa'),
        ('APTO', 'Apartamento'),
        ('SALA', 'Sala'),
        ('OUTRO', 'Outro'),
    ]

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=15)
    genero = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.PositiveBigIntegerField(max_length=100)
    complemento = models.CharField(
        max_length=15,
        choices=COMPLEMENTOS,
        blank=False,
        null=True
    )
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    CEP = models.CharField(max_length=10, default='00000000')
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome} ({self.cidade})'