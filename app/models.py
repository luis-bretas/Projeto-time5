from django.db import models

# Create your models here.
from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    pontos = models.IntegerField(default=0)
    sequencia = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=50)
    pontos = models.IntegerField()

    def __str__(self):
        return self.tipo