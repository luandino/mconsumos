from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)


class Factura(models.Model):
    tipo = models.CharField(max_length=2)
    local = models.IntegerField()
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

