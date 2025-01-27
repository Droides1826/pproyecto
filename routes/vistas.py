from utils.db import conexion
from flask import Blueprint, jsonify, render_template, request, url_for

vistas = Blueprint('vistas', __name__)

@vistas.route('/')
def index():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT p.id_producto, p.nombre, p.nombre_imagen, p.descripcion FROM productos p ORDER BY RAND() LIMIT 8')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    productos = []
    for row in data:
        producto = dict(zip(columnas, row))
        productos.append(producto)
    return render_template('index.html', productos=productos)

@vistas.route('/ferreteria')
def ferreteria():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE `id_categoria`= 1;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return render_template('ferreteria.html', categorias=categorias)

@vistas.route('/comida')
def comida():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE `id_categoria`= 2;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return render_template('comida.html', categorias=categorias)

@vistas.route('/mascotas')
def mascotas():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE `id_categoria`= 3;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return render_template('mascotas.html', categorias=categorias)

@vistas.route('/vehiculos')
def vehiculos():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE `id_categoria`= 4;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return render_template('vehiculos.html', categorias=categorias)

@vistas.route('/hogar')
def hogar():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE `id_categoria`= 5;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return render_template('hogar.html', categorias=categorias)