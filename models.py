from django.db import models

# Create your models here.
class Clientes(models.Model):
    cliente = models.CharField(max_length=150)
    sexo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.IntegerField()