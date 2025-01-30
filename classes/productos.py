from utils import db
import app

class producto_clase:
    
    def __init__(self):
        self.conexion = db.conexion.connection.cursor()
    
    def mostrar_producto(self, productos):
        if productos:
            query = 'SELECT * FROM `productos` WHERE productos = %s;'
            self.conexion.execute(query, (productos,))
        else:
            query = 'SELECT * FROM `productos`;'
            self.conexion.execute(query)
        
        data = self.conexion.fetchall()
        columnas = [desc[0] for desc in self.conexion.description]
        productos = []
        for row in data:
            producto = dict(zip(columnas, row))
            productos.append(producto)
        return productos
    
    def mostrar_producto_por_categoria(self, id_categoria):
        query = 'SELECT * FROM `productos` WHERE `id_categoria` = %s;'
        self.conexion.execute(query, (id_categoria,))
        data = self.conexion.fetchall()
        columnas = [desc[0] for desc in self.conexion.description]
        productos = []
        for row in data:
            producto = dict(zip(columnas, row))
            productos.append(producto)
        return productos
    
    def agregar_producto(self, nombre_producto, precio, id_categoria ):
        query = 'INSERT INTO `productos` (`nombre`, `descripcion`, `precio`, `id_categoria`, `cantidad`, `nombre_imagen`) VALUES (%s, %s, %i, %i, %i, %s);'
        self.conexion.execute(query, (nombre_producto, precio, id_categoria))
        db.conexion.connection.commit()
        return {"mensaje": "Producto agregado correctamente"}, 200
    

