from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('busca', views.busca, name='busca'),
    path('criar/receita', views.criar_receita, name='criar_receita'),
    path('<int:receita_id>', views.deletar_receita, name='deletar_receita'),
    path('editar/<int:receita_id>', views.editar_receita, name='editar_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita')
]
