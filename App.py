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
app.config['MYSQL_DB'] = 'tallertres'
#Ejecutamos el módulo MySQL con las configuraciones 
mysql = MySQL(app)
#Cambiamos ruta para evitar que el servidor arroje un Error 404
@app.route('/')
#Creamos una función para manejar la ruta
def Index():
    #Retornamos con render_template una vista llamada index.html, la cual es una plantilla HTML ubicada en la carpeta Vistas
    return render_template('index.html')
#Ruta para añadir clientes
@app.route('/addClient')
#Creamos una función para manejar la ruta
def addClient():
    #Guardamos datos pero primero hacemos una comprobación
    if request.method == 'POST':
        #Guardamos cada dato en una variable
        documento = request.form['documento']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fechaNacimiento = request.form['fechaNacimiento']
        correo = request.form['correo']
        numeroTelefono = request.form['numeroTelefono']
        #Usamos conexión a MySQL para insertar los datos en la BD
        #Usamos un cursor para saber donde está la conexión
        cur = mysql.connection.cursor()
        #Armamos la sentencia SQL, los valores los ponemos con %s y luego armamos una tupla para poner las variables
        cur.execute('INSERT INTO clientes (documento, nombre, apellido, fechaNacimento, correo, numeroTelefono) VALUES (%s, %s, %s, %s, %s, %s)', (documento, nombre, apellido, fechaNacimiento, correo, numeroTelefono, numeroTelefono))
        #Ejecutamos la sentencia SQL
        mysql.connection.commit()
        print("Documento: ", documento)
        print("Nombre: ", nombre)
        print("Apellido: ", apellido)
        print("FechaNacimiento: ", fechaNacimiento)
        print("Correo: ", correo)
        print("NumeroTelefono: ", numeroTelefono)
        #return 'sent'
        #Usamos redirect y url_for para redireccionar
        return redirect(url_for('Index'))
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