from utils.db import conexion
from classes.vistas import vistas_clase
from classes.productos import producto_clase
from flask import Blueprint, jsonify, render_template, request, url_for, current_app

vistas = Blueprint('vistas', __name__)

@vistas.route('/')
def index():
    vistas_obj = vistas_clase()
    try:
        productos = vistas_obj.index()
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@vistas.route('/home', methods=['GET', 'POST'])
def home():
    control_id = request.args.get('control_id')
    vistas_obj = vistas_clase()
    try:
        productos = vistas_obj.home(control_id)
        return jsonify(productos), 200
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



