from django.db import models

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    imagem = models.CharField(max_length=512)
    preco = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = "itens"
