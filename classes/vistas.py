from utils import db
from flask import Blueprint, jsonify

class vistas_clase:
    def __init__(self):
        self.conexion = db.conexion.connection.cursor()
    
    def index(self):
        query = 'SELECT p.id_producto, p.nombre, p.nombre_imagen, p.descripcion FROM productos p ORDER BY RAND() LIMIT 8'
        try:
            self.conexion.execute(query)
            data = self.conexion.fetchall()
            columnas = [desc[0] for desc in self.conexion.description]
            productos = []
            for row in data:
                producto = dict(zip(columnas, row))
                productos.append(producto)
            return productos
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def home(self, control_id):
        query = 'SELECT * FROM productos WHERE id_categoria = %s;'
        try:
            self.conexion.execute(query, (control_id,))
            data = self.conexion.fetchall()
            columns = [desc[0] for desc in self.conexion.description]
            products = [dict(zip(columns, row)) for row in data]
            return products
        except Exception as e:
            return jsonify({"error": str(e)}), 500
