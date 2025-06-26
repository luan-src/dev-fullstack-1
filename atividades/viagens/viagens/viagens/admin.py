from django.contrib import admin
from .models import Viagem


@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'destino', 'data_partida', 'preco',)
    search_fields = ('destino',)
    list_filter = ('destino',)
