from django.contrib import auth, messages
from django.shortcuts import render, redirect
from AluraReceitas.Functions import Authenticate
from django.contrib.auth.models import User
from typing import Dict
from apps.Receitas.models import Receita


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

