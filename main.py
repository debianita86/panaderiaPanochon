import mysql.connector
from flask import Flask
from flask import request, jsonify
from flask import render_template
from flask import url_for
from flask import redirect

config ={
    "user":"AdminPan",
    "host":"localhost",
    "password":"Admin123.",
    "database":"Panaderia",
    "raise_on_warnings":True
}

appPanaderia = Flask(__name__)

@appPanaderia.route("/productopanaderia", methods=["GET"])
def index():
    if request.method == "GET":
        conexion = mysql.connector.connect(**config)
        miCursor =  conexion.cursor()
        query = "SELECT * FROM productos"
        miCursor.execute(query)
        resultado = miCursor.fetchall()
        conexion.commit()
        miCursor.close()
        conexion.close()
    return render_template("index.html", results=resultado)

@appPanaderia.route("/productopanaderia", methods=["POST"])
def insertar_productos():
    if request.method=="POST":
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = 1 if request.form.get('stock') else 0
        conexion = mysql.connector.connect(**config)
        miCursor = conexion.cursor()
        query = "insert into productos(nombre, precio, stock) values (%s,%s,%s)"
        val = (nombre, precio, stock)
        miCursor.execute(query, val)
        conexion.commit()
        miCursor.close()
        conexion.close()
        return redirect('/productopanaderia')
    return render_template('crear-producto.html')

@appPanaderia.route('/guardar-edicion/<string:id>', methods=['GET'])
def guardar_edicion(id):
    if request.method=='GET':
        conexion = mysql.connector.connect(**config)
        miCursor = conexion.cursor()
        query = 'select * from productos where idProducto=%s'
        val = (id,)
        miCursor.execute(query, val)
        resultado = miCursor.fetchone()
        conexion.commit()
        miCursor.close()
        conexion.close()
        return render_template('editar-producto.html', results=resultado)
    return render_template('crear-producto.html')

@appPanaderia.route('/productopanaderia/<string:id>', methods=['POST'])
def editar_producto(id):
    nombre = request.form['nombre']
    precio = request.form['precio']
    stock = 1 if request.form.get('stock') else 0
    conexion = mysql.connector.connect(**config)
    miCursor = conexion.cursor()
    query = 'UPDATE productos SET precio=%s, stock=%s WHERE idProducto=%s'
    val = (precio, stock, id)
    miCursor.execute(query, val)
    conexion.commit()
    miCursor.close()
    conexion.close()
    return redirect('/productopanaderia')


@appPanaderia.route('/eliminarproducto/<string:id>', methods=['GET', 'POST'])
def eliminar_producto(id):
    if request.method=='GET':
        conexion = mysql.connector.connect(**config)
        miCursor = conexion.cursor()
        query= 'select * from productos where idProducto=%s'
        val = (id,)
        miCursor.execute(query, val)
        resultado = miCursor.fetchone()
        conexion.commit()
        miCursor.close()
        conexion.close()
        return render_template('eliminar-producto.html', results=resultado)
    elif request.method=='POST':
        conexion = mysql.connector.connect(**config)
        miCursor = conexion.cursor()
        query= 'DELETE from productos where idProducto=%s'
        val=(id,)
        miCursor.execute(query, val)
        conexion.commit()
        miCursor.close()
        conexion.close()
        return redirect('/productopanaderia')



if __name__== "__main__":
    appPanaderia.run(debug=True)