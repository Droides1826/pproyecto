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

@categorias.route('/ferreteria', methods=['GET'])
def ferreteria():
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT * FROM `categorias` WHERE nombre_categoria = "Ferreteria";')
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    categorias = []
    for row in data:
        categoria = dict(zip(columnas, row))
        categorias.append(categoria)
    return render_template('ferreteria.html', data=categorias)
    
