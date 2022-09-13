from django.db import models


class Produto(models.Model):
    produto = models.CharField(max_length=40)
    preco = models.CharField(max_length=40)
    descricao = models.CharField(max_length=60)

