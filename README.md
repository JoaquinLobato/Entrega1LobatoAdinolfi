
# Pre-Entega Desafio Final de Joaquin Lobato Adinolfi


La entrega apunta a mostrar lo aprendido hasta el momento en clase. Manejo de Python y Django. 


## Para Comenzar


Previo a poder utilizar la pagina se debe crear un ambiente virtual en la terminal con la linea de codigo:


```sh
python -m venv (segudio del nombre que se le quiera asignar al ambiente virtual)
```


Luego, se debe instalar Django con otro codigo en la terminal:

```sh
pip install Django
```


Y por ultimo, por necesidad de mi proyecto, se debe instalar la libreria de money de Django con el codigo:
```sh
pip install django-money
```


Con todo ello instalado, ya se puede mover a la carpeta que contiene el archivo manage.py con el que se podra correr el servido. Para ello se usa en la terminal:
```sh
cd /Entega/Entrega_final1
```

Y una vez alli, posicionados en la carpeta se utilizan los codigos:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Con ello ya estaria corriendo el servidor y la pagina.


## Sobre el Proyecto y sus Funcionalidades


Contiene distintas funciones, las cuales se ven reflejada como botones en la pagina y las cuales fueron realizadas dentro de la app Negocio

### Crear Empleado

Con ella, se puede registrar un nuevo empleado a la base de datos a traves de una form. Esta form toma los datos del modelo Empleados (que se encuentra en el archivo models.py de la app Negocio) y cuenta con la posibilidad de registrar el nombre, apellido, email, id, sueldo y puesto del empleado.


### Registrar Producto


Similar a crear empleado, esta funcion deja registrar el nombre, el id y el precio de un producto que se vende en el negocio. La form del mismo se encuentra en forms.py de la app negocio y contiene los datos de la class Productos de models.py

### Registrar Stock

Al igual que las anteriores, permite registrar a la base de datos el Stock del negocio.


### Herencia 


Se pretende con la misma mostrar lo aprendido en clase sobre la herencia de templates. La misma toma la templete index.html como base, hereda parte de ella pero contiene un cambio.

### Buscar Empleado

Pemite, conociendo el ID de los empleados, buscar los datos del ID que coincida con el introducido.





