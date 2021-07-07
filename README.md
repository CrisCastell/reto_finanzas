# Instrucciones para aplicacion
Una vez descargadas las carpetas se necesita hacer 3 procedimientos por separado ya que se deben ejecutar en servidores distintos

## Base de datos
1- descargar la base de datos y correrla en un servidor local (localhost) en el puerto 5432. Las credenciales para la base de datos estan en el archivo "credenciales"
Por ser una prueba y una base de datos ficticia, las credenciales de la base de datos estan ya escritas en la aplicacion con Django, por lo que no es necesario agregarlas

## React
1- ingresar a "reto-FE" y correr el comando "npm install" para instalar las librerias necesarias para correr la aplicacion. O simplemente ejecutar "npm install axios" ya que es la unica libreria que esta instalada para esta prueba


## Django 
1- Ingresar a la carpeta llamada reto_BE, y crear un python enviroment con el siguiente comando "python -m venv env", y una vez creado ejecutar el comando "env/Scripts/activate" para inciar el enviroment. PUede ocurrir el caso que Windows no tenga permisos para ejecutar ese comando, pero aun se puede proceder con el paso 3
2- Ingresar a la carpeta retoFinanzas y ejecutar el comando "pip install -r requirements.txt". Esto instalara las librerias necesarias para correr el proyecto exitosamente.

3- ejecutar el comando python manage.py runserver

Nota: para correr la aplicacion con de frontend ejecutar "npm start"

Ambas partes del proyecto se ejecutaran en el servidor local por defecto. En caso de React http://localhost:3000, y en caso de Django http://127.0.0.1:8000
