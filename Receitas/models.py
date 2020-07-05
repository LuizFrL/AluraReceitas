from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=50)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.TextField()
    dia_preparo = models.DateField(default=datetime.now, blank=True)
    publicar = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

