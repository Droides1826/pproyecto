from utils import db
from flask import Blueprint, jsonify

class vistas_clase:
    def __init__(self):
        self.conexion = db.conexion.connection.cursor()
    
    def index(self):
        query = '''
            SELECT p.id_producto, p.nombre, p.nombre_imagen, p.id_categoria, precio,
                c.nombre_categoria, p.descripcion, p.cantidad
            FROM productos p
            JOIN categorias c ON p.id_categoria = c.id_categoria
            WHERE p.cantidad > 0
            ORDER BY RAND() 
            LIMIT 8;
        '''
        try:
            self.conexion.execute(query)
            data = self.conexion.fetchall()
            columnas = [desc[0] for desc in self.conexion.description]
            productos = [dict(zip(columnas, row)) for row in data]
            return productos  
        except Exception as e:
            return {"error": str(e)}, 500 
    
    
    def consultas(self):
        query = '''
            SELECT p.id_producto, p.nombre, p.nombre_imagen, p.id_categoria, 
                c.nombre_categoria, p.descripcion, p.precio, p.cantidad
            FROM productos p
            JOIN categorias c ON p.id_categoria = c.id_categoria WHERE p.cantidad > 0;
        '''
        try:
            self.conexion.execute(query)
            data = self.conexion.fetchall()
            columnas = [desc[0] for desc in self.conexion.description]
            productos = [dict(zip(columnas, row)) for row in data]
            return productos  
        except Exception as e:
            return {"error": str(e)}, 500 
    
    def home(self, control_id):
        query = 'SELECT * FROM productos WHERE id_categoria = %s;'
        try:
            self.conexion.execute(query, (control_id,))
            data = self.conexion.fetchall()
            columns = [desc[0] for desc in self.conexion.description]
            products = [dict(zip(columns, row)) for row in data]
            return products
        except Exception as e:
            return {"error": str(e)}, 500
