from utils.db import conexion
from classes.vistas import vistas_clase
from classes.productos import producto_clase
from flask import Blueprint, jsonify, render_template, request

vistas = Blueprint('vistas', __name__)

@vistas.route('/')
def index():
    return render_template('index.html')

@vistas.route('/hogar')
def hogar():
    return render_template('hogar.html')

@vistas.route('/comida')
def comida():
    return render_template('comida.html')

@vistas.route('/mascotas')
def mascotas():
    return render_template('mascotas.html')

@vistas.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@vistas.route('/ferreteria')
def ferreteria():
    return render_template('ferreteria.html')

@vistas.route('/home', methods=['GET', 'POST'])
def home():
    vistas_obj = vistas_clase()
    try:
        productos = vistas_obj.index()
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@vistas.route('/consulta', methods=['GET', 'POST'])
def consulta():
    vistas_obj = vistas_clase()
    try:
        productos = vistas_obj.consultas()
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@vistas.route('/productos/<int:id_categoria>', methods=['GET'])
def mostrar_producto_por_categoria(id_categoria):
    productos_obj = producto_clase()
    try:
        productos = productos_obj.mostrar_producto_por_categoria(id_categoria)
        return jsonify(productos)
    except Exception as e:
        return jsonify("error"), 500