from utils import db
from utils.db import conexion

class categorias_clase:
    
    @classmethod
    def __init__(self):
        self.conexion = db.conexion.connection.cursor()

    # esta funcion permite consultar todas las categorias ingresadas en la base de datos
    @classmethod
    def consulta_categoria(self):
        query = ('SELECT * FROM `categorias`')
        self.conexion.execute(query)
        data = self.conexion.fetchall()
        columnas = [desc[0] for desc in self.conexion.description]
        categorias = []
        for row in data:
            categoria = dict(zip(columnas, row))
            categorias.append(categoria)
        return categorias
    
    # esta funcion permite agregar una categoria a la base de datos
    @classmethod
    def agregar_categoria(self, nombre_categoria, descripcion):
        query = 'INSERT INTO `categorias` (`nombre_categoria`, `descripcion` ) VALUES (%s, %s);'
        self.conexion.execute(query, (nombre_categoria, descripcion,))
        conexion.connection.commit()
        return {"mensaje": "Categoria agregada correctamente"}, 200