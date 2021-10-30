from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=20)
    imagem = models.CharField(max_length=256)
    preco = models.CharField(max_length=20)
    class Meta:
        db_table = "itens"
