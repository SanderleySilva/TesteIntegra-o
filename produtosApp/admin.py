from django.contrib import admin
from .models import ProdutosCad

@admin.register(ProdutosCad)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco_cartao', 'preco_pix']

