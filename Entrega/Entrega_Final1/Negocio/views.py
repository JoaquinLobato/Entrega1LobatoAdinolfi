from django.shortcuts import render
from .models import Empleados, Productos, Stock
from django import forms
from .forms import RegistrarProducto
# Create your views here.

def test(request):
    return render(request, 'Negocio/index.html')

#Carga de datos de empleados a la BD, a traves de forms
class CrearEmpleado_test(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'

def CrearEmp(request):
    if request.method == 'POST':
        form = CrearEmpleado_test(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Negocio/index.html')
    else:
        form = CrearEmpleado_test

    return render(request, 'Negocio/crear_empleado.html', {'form': form})

#Prueba/Desafio de herencia de HTML
def Herencia(request):
    return render(request, 'Negocio/herencia.html')

#Boton para volver al inicio
def Home(request):
    return render(request, 'Negocio/index.html')

#Registro de Productos a la BD

def Registro_Producto(request):

    if request.method == 'POST':
        
        form = RegistrarProducto(request.POST)
        
        if form.is_valid():
        
            clean_form = form.cleaned_data

            producto = Productos(nombre_producto=clean_form['nombre_producto'], id_producto=clean_form['id_producto'], precio=clean_form['precio'])
        
            producto.save()
            
            return render(request, 'Negocio/index.html')
    else:
        form = RegistrarProducto()

    return render(request, 'Negocio/registrar_productos.html', {'form': RegistrarProducto})

#Registro de Stock a traves de forms
class RegistrarStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'

def RegStock(request):
    if request.method == 'POST':
        form = RegistrarStock(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Negocio/index.html')
    else:
        form = RegistrarStock

    return render(request, 'Negocio/registrar_stock.html', {'form': form})

#Busqueda de empleado de la BD
def buscar_empleado(request): 

    if request.GET.get('id_empleado', False):

        id_empleado = request.GET['id_empleado']
        empleados = Empleados.objects.filter(id_empleado__icontains = id_empleado)

        return render(request, 'Negocio/buscar_empleado.html', {'empleados': empleados})
    else:
        respuesta = 'No hay datos para este ID'

    return render(request, 'Negocio/buscar_empleado.html', {'respuesta': respuesta})
    