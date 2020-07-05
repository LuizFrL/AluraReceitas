from django.contrib import auth, messages
from django.shortcuts import render, redirect, get_object_or_404
from AluraReceitas.Functions import Authenticate
from django.contrib.auth.models import User
from typing import Dict
from Receitas.models import Receita


# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form: Dict[str, str] = request.POST
        nome: str = form['nome']
        email: str = form['email']
        senha: str = form['password']
        senha2: str = form['password2']
        if Authenticate(request).user_authenticate(email, senha, senha2) and nome.strip():
            user = User.objects.create_user(nome, email, senha)
            user.save()
            print('Usuario cadastrado com Sucesso!')
            return redirect('login')
    return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        form: Dict[str, str] = request.POST
        email: str = form['email']
        senha: str = form['senha']
        usuario = User.objects.filter(email=email)
        if usuario.exists():
            username = usuario.values_list('username', flat=True).get()
            user_auth = auth.authenticate(request, username=username, password=senha)
            if user_auth is not None:
                auth.login(request, user_auth)
                return redirect('dashboard')
            messages.error(request, 'Não foi possível realizar login, senha incorreta!')
        messages.error(request, 'Email informado está incorreto')
    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-dia_preparo').filter(pessoa_id=request.user.id)
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


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
    return render(request, 'usuarios/criar_receitas.html')


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
            return render(request, 'usuarios/editar_receita.html', dados)
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