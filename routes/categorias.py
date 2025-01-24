from utils.db import conexion
from flask import Blueprint, render_template, jsonify

categorias = Blueprint('categorias', __name__)

@categorias.route('/mostrar_categorias', methods=['GET'])
def mostrar_categorias():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `categorias` WHERE 1;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return jsonify(categorias) 

@categorias.route('/hogar', methods=['GET'])
def hogar():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE id_categoria = 1;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return jsonify(categorias)

@categorias.route('/comida', methods=['GET'])
def comida():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE id_categoria = 2;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return jsonify(categorias)

@categorias.route('/mascotas', methods=['GET'])
def mascotas():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE id_categoria = 3;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return jsonify(categorias)

@categorias.route('/vehiculos', methods=['GET'])
def vehiculos():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE id_categoria = 4;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return jsonify(categorias)

@categorias.route('/ferreteria', methods=['GET'])
def ferreteria():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `productos` WHERE id_categoria = 5;')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return jsonify(categorias)