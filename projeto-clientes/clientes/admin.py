from django.contrib import admin
from .models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cidade', 'data_registro')
    readonly_fields = ('data_registro',)
    search_fields = ('nome', 'sobrenome', 'cidade')