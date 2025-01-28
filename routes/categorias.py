from utils.db import conexion
from flask import Blueprint, render_template, jsonify, request
from classes.categorias import categorias_clase

categorias = Blueprint('categorias', __name__)

@categorias.route('/mostrar_categorias', methods=['GET'])
def mostrar_categorias():
    id_categoria = request.args.get('id_categoria', 2)
    categorias_obj = categorias_clase()
    categorias = categorias_obj.mostrar_categorias(id_categoria)
    return jsonify(categorias=categorias)

