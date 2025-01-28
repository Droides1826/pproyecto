import os
import time
from utils.db import conexion
from flask import Blueprint, jsonify, render_template, request, url_for
from classes.productos import producto_clase

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

