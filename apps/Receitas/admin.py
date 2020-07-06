from django.contrib import admin
from .models import Receita


class ListagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'publicar')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita', )
    list_filter = ('tempo_preparo', )
    list_editable = ('publicar', )
    list_per_page = 5


# Register your models here.
admin.site.register(Receita, ListagemAdmin)
