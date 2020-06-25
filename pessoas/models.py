from django.db import models


# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
