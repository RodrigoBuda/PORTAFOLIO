from django.db import models

# Create your models here.

class Vendedor(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
    
class Compra(models.Model):
    producto = models.CharField(max_length=30)
    precio = models.IntegerField()
    enviado = models.BooleanField()
    
