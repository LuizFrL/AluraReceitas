from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from .models import Receita
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request: WSGIRequest):
    receitas = Receita.objects.order_by('-dia_preparo').filter(publicar=True)
    paginator = Paginator(receitas, 2)
    page = request.GET.get('page')
    receita_por_pagina = paginator.get_page(page)

    dados: dict = {
        'receitas': receita_por_pagina
    }
    return render(request, 'receitas/index.html', dados)


def receita(request: WSGIRequest, receita_id: int):
    dados: dict = {
        'inf_receita': get_object_or_404(Receita, pk=receita_id)
    }
    return render(request, 'receitas/receita.html', dados)


def busca(request):
    receitas = Receita.objects.order_by('-dia_preparo').filter(publicar=True)
    receita_a_buscar = request.GET['search']
    if receita_a_buscar:
        receitas = receitas.filter(nome_receita__icontains=receita_a_buscar)

    dados = {
        'receitas': receitas
    }
    return render(request, 'receitas/busca.html', dados)


def criar_receita(request):
    if request.method == 'POST':
        nome = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_prep = request.POST['modo_preparo']
        tempo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        foto = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user, nome_receita=nome,
                                         ingredientes=ingredientes, modo_preparo=modo_prep,
                                         tempo_preparo=tempo, rendimento=rendimento,
                                         imagem=foto)
        receita.save()
        return redirect('dashboard')
    return render(request, 'receitas/criar_receitas.html')


def deletar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def editar_receita(request, receita_id):
    receita = Receita.objects.filter(id=receita_id).get()
    if request.user.is_authenticated:
        if request.user.id == receita.pessoa_id:
            dados = {
                'receita': receita
            }
            return render(request, 'receitas/editar_receita.html', dados)
    return redirect('index')


def atualiza_receita(request):
    if request.method == 'POST':
        id_receita = request.POST['receita_id']
        receita = Receita.objects.get(pk=id_receita)
        receita.nome_receita = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_preparo = request.POST['modo_preparo']
        receita.tempo_preparo = request.POST['tempo_preparo']
        receita.rendimento = request.POST['rendimento']
        if request.FILES.get('foto_receita'):
            receita.imagem = request.FILES.get('foto_receita')

        receita.save()
    return redirect('dashboard')
