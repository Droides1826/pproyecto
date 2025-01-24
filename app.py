from flask import Flask, jsonify, render_template
from utils.db import conexion
from routes.productos import productos
from routes.categorias import categorias

app = Flask(__name__, template_folder='template')

#conexion a la base de datoss
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pproyecto'
conexion.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos_por_categoria/<int:id_categoria>', methods=['GET'])
def productos_por_categoria(id_categoria):
    MySQL = conexion.connection.cursor()
    MySQL.execute('SELECT p.id_producto, p.nombre, p.descripcion, p.precio, p.estado, c.nombre_categoria, p.cantidad FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria WHERE c.id_categoria = %s;', (id_categoria,))
    data = MySQL.fetchall()
    columnas = [desc[0] for desc in MySQL.description]
    productos = []
    for row in data:
        producto = dict(zip(columnas, row))
        productos.append(producto)
    return jsonify(productos)

app.register_blueprint(productos)
app.register_blueprint(categorias)