#Llamamos al framework de Flask y las funciones render_template, request, redirect, url_for y fkas
from flask import Flask, render_template, request, redirect, url_for, flash
#Importamos el respectivo módulo de Flask para conectarnos a MySQL
from flask_mysqldb import MySQL
#Configuramos la conexión
app = Flask(__name__)
#Configuramos los parámetros para la conexión a MySQL
#Host del servidor MySQL
app.config['MYSQL_HOST'] = 'localhost'
#Usuario del servidor MySQL
app.config['MYSQL_USER'] = 'root'
#Contraseña del servidor MySQL
app.config['MYSQL_PASSWORD'] = ''
#Base de datos que tenemos en el servidor MySQL
app.config['MYSQL_DB'] = 'test'
#Ejecutamos el módulo MySQL con las configuraciones 
mysql = MySQL(app)
#Cambiamos ruta para evitar que el servidor arroje un Error 404
@app.route('/')
#Creamos una función para manejar la ruta
def Index():
    return "Principal Route"
#Ruta para añadir clientes
@app.route('/addClient')
#Creamos una función para manejar la ruta
def addClient():
    return "Add Client Route"
#Ruta para listar clientes
@app.route('/listClients')
#Creamos una función para manejar la ruta
def listClients():
    return "List Clients Route"
#Ruta para actualizar clientes
@app.route('/updateClient')
#Creamos una función para manejar la ruta
def updateClients():
    return "Update Clients Route"
#Ruta para eliminar clientes
@app.route('/deleteClient')
#Creamos una función para manejar la ruta
def deleteClient():
    return "Delete Clients Route"
#Comprobamos si el archivo que ese está ejecutando es el principal
if __name__ == '__main__':
    '''
    Asignamos puertos y para reiniciar constantemente el servidor
    cada vez que guardemos cambios usamos el parámetro debug=True
    '''
    app.run(port=3000, debug=True)