from django.contrib import admin
from pessoas.models import Pessoas


class ListagemPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')
    list_per_page = 5


# Register your models here.
admin.site.register(Pessoas, ListagemPessoas)
