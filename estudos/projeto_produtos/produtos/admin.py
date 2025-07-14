from django.contrib import admin
from .models import Produto

# Register your models here.

@admin.register(Produto)
class AdminProduto(admin.ModelAdmin):
    list_display = ("nome", "descricao", "preco")
    search_fields = ("nome",)
    list_per_page = 10