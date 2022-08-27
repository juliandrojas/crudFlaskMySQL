#Llamamos al framework de Flask y las funciones render_template, request, redirect, url_for y fkas
from flask import Flask, render_template, request, redirect, url_for, flash
#Configuramos la conexión
app = Flask(__name__)
#Cambiamos ruta para evitar que el servidor arroje un Error 404
@app.route('/')
#Creamos una función para manejar las rutas
def Index():
    print("Principal Route")
#Comprobamos si el archivo que ese está ejecutando es el principal
if __name__ == '__main__':
    '''
    Asignamos puertos y para reiniciar constantemente el servidor
    cada vez que guardemos cambios usamos el parámetro debug=True
    '''
    app.run(port=3000, debug=True)