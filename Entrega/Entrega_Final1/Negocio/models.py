from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
class Empleados(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    id_empleado = models.IntegerField()
    sueldo = MoneyField(max_digits=14, decimal_places=2, default_currency='ARS')
    puesto = models.CharField(max_length=50)

class Productos(models.Model):

    nombre_producto = models.CharField(max_length=40)
    id_producto = models.IntegerField()
    precio = models.IntegerField()

class Stock(models.Model):

    nombre_articulo = models.CharField(max_length=40)
    id_articulo = models.IntegerField()
    cantidad_actual = models.IntegerField()
    precio_unidad = MoneyField(max_digits=12, decimal_places=2, default_currency='ARS')