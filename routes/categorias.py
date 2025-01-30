from utils.db import conexion
from flask import Blueprint, render_template, jsonify, request
from utils.utils import respuesta_json
from classes.categorias import categorias_clase

categorias = Blueprint('categorias', __name__)

# esta api permite consultar todas las categorias ingresadas en la base de datos
@categorias.route('/mostrar_categorias', methods=['GET'])
def mostrar_categorias():
    id_categoria = request.args.get('id_categoria')
    categorias_obj = categorias_clase()
    categorias = categorias_obj.mostrar_categorias(id_categoria)
    return respuesta_json(categorias, "Consulta exitosa", 200)

# esta api permite agregar una categoria a la base de datos
@categorias.route('/agregar_categoria', methods=['POST'])
def agregar_categoria():
    nombre_categoria = request.json['nombre_categoria']
    descripcion = request.json['descripcion']
    categorias_obj = categorias_clase()
    try:
        categorias_obj.agregar_categoria(nombre_categoria, descripcion)
        return respuesta_json({}, "Categoria agregada correctamente", 200)
    except Exception as e:
        return respuesta_json({}, "Error al agregar la categoria", 500)