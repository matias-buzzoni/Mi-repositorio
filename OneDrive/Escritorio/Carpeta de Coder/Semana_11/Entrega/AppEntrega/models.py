from django.db import models

# Create your models here.

class Vendedor(models.Model):
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=30)



class Mayorista(models.Model):
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)



