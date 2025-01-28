from utils import db
import app

class categorias_clase:
    
    @staticmethod
    def __init__(self):
        self.conexion = db.conexion.connection.cursor()
    
    @staticmethod
    def mostrar_categorias(self, id_categoria):
        if id_categoria:
            query = 'SELECT * FROM `categorias` WHERE id_categoria = %s;'
            self.conexion.execute(query, (id_categoria,))
        else:
            query = 'SELECT * FROM `categorias`;'
            self.conexion.execute(query)
        
        data = self.conexion.fetchall()
        columnas = [desc[0] for desc in self.conexion.description]
        categorias = []
        for row in data:
            categoria = dict(zip(columnas, row))
            categorias.append(categoria)
        return categorias

