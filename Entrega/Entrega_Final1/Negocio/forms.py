from django import forms
from djmoney.models.fields import MoneyField

class CrearEmpleado(forms.Form): #form no utilizado ya que no encontre la forma de aplicar el MoneyField.

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    id_empleado = forms.IntegerField()
    sueldo = MoneyField(max_digits=14, decimal_places=2, default_currency='ARS')
    puesto = forms.CharField(max_length=50)

class RegistrarProducto(forms.Form):

    nombre_producto = forms.CharField(max_length=40)
    id_producto = forms.IntegerField()
    precio = forms.IntegerField()