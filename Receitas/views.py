from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Receita
from typing import List
# Create your views here.


def index(request: WSGIRequest):
    receitas = Receita.objects.order_by('-dia_preparo').filter(publicar=True)
    dados: dict = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request: WSGIRequest, receita_id: int):
    dados: dict = {
        'inf_receita': get_object_or_404(Receita, pk=receita_id)
    }
    return render(request, 'receita.html', dados)


def busca(request):
    receitas = Receita.objects.order_by('-dia_preparo').filter(publicar=True)
    receita_a_buscar = request.GET['search']
    if receita_a_buscar:
        receitas = receitas.filter(nome_receita__icontains=receita_a_buscar)

    dados = {
        'receitas': receitas
    }
    return render(request, 'busca.html', dados)
