from utils.db import conexion
from flask import Blueprint, jsonify

productos = Blueprint('productos', __name__)

@productos.route('/mostrar_productos', methods=['GET'])
def mostrar_productos():
    MySQL = conexion.connection.cursor()
    MySQL.execute(' SELECT p.id_producto, p.nombre, p.descripcion, p.precio, p.estado, c.nombre_categoria,  p.cantidad FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria WHERE 1; ')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    productos = []
    for row in data:
        producto = dict(zip(columnas, row))
        productos.append(producto)
    return jsonify(productos)

@productos.route('/productos_por_categoria/<int:id_categoria>', methods=['GET'])
def productos_por_categoria(id_categoria):
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT p.id_producto, p.nombre, p.descripcion, p.precio, p.estado, c.nombre_categoria, p.cantidad FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria WHERE c.id_categoria = %s;', (id_categoria,))
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    productos = []
    for row in data:
        producto = dict(zip(columnas, row))
        productos.append(producto)
    return jsonify(productos)