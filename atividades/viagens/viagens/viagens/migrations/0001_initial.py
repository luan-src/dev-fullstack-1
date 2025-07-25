# Generated by Django 5.2.3 on 2025-06-26 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=100)),
                ('data_partida', models.DateField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('clientes', models.ManyToManyField(related_name='viagens', to='clientes.cliente')),
            ],
        ),
    ]
