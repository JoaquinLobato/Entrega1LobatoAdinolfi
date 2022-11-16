from django.urls import path
from Negocio import views

urlpatterns = [
    path('', views.test),
    path('crear_empleado/', views.CrearEmp, name='Crear Empleado'),
    path('herencia/', views.Herencia, name='Herencia'),
    path('home/', views.Home, name='Home'),
    path('registrar_productos/', views.Registro_Producto, name='Registrar Producto'),
    path('registrar_stock/', views.RegStock, name='Registrar Stock'),
    path('buscar_empleado/', views.buscar_empleado, name='Buscar Empleado')
]
