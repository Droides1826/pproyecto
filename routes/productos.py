from utils.db import conexion
from flask import Blueprint, jsonify, render_template, request, url_for
import os
import time

productos = Blueprint('productos', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@productos.route('/producto', methods=['POST'])
def agregar_producto():
    if 'image' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        extension = file.filename.rsplit('.', 1)[1].lower()
        filename = f"producto_{int(time.time())}.{extension}"
        filepath = os.path.join('static', 'uploads', filename)
        
        file.save(filepath)

        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        id_categoria = request.form['id_categoria']
        cantidad = request.form['cantidad']

        cur = conexion.connection.cursor()
        cur.execute("""
            INSERT INTO productos (nombre, descripcion, precio,  id_categoria, cantidad, nombre_imagen)
            VALUES (%s, %s, %s, %s, %s, %s, )
        """, (nombre, descripcion, precio, id_categoria, cantidad, filename))
        conexion.connection.commit()
        cur.close()

        return jsonify({'message': 'Producto agregado correctamente'}), 201

    return jsonify({'message': 'Invalid file format'}), 400

@productos.route('/mostrar_productos', methods=['GET'])
def mostrar_productos():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT p.id_producto, p.nombre, p.descripcion, p.precio, p.estado, c.nombre_categoria, p.cantidad FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria ORDER BY RAND() LIMIT 8;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    productos = [dict(zip(columnas, row)) for row in data]
    return jsonify(productos)

@productos.route('/productos_por_categoria/<int:id_categoria>', methods=['GET'])
def productos_por_categoria(id_categoria):
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT p.id_producto, p.nombre, p.descripcion, p.precio, p.estado, c.nombre_categoria, p.cantidad FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria WHERE c.id_categoria = %s;', (id_categoria,))
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    productos = [dict(zip(columnas, row)) for row in data]
    return jsonify(productos)

@productos.route('/buscar_producto/<nombre>', methods=['GET'])
def buscar_producto(nombre):
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM productos WHERE nombre LIKE %s;', (f"{nombre}%",))
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    productos = [dict(zip(columnas, row)) for row in data]
    
    if productos == []:
        return jsonify({'message': 'Producto no encontrado'}), 404
    return jsonify(productos)

