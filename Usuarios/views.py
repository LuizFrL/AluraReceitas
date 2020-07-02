from django.shortcuts import render, redirect
from AluraReceitas.Functions import Authenticate
from django.contrib.auth.models import User
from typing import Dict


# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form: Dict[str, str] = request.POST
        nome: str = form['nome']
        email: str = form['email']
        senha: str = form['password']
        senha2: str = form['password2']
        if Authenticate().user_authenticate(email, senha, senha2) and nome.strip():
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
        return redirect('dashboard')
    return render(request, 'usuarios/login.html')


def logout(request):
    return None


def dashboard(request):
    return None
