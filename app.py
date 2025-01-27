from flask import Flask
from utils.db import conexion
from routes.vistas import vistas
from routes.productos import productos
from routes.categorias import categorias

app = Flask(__name__, template_folder='template')

#conexion a la base de datoss
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pproyecto'
conexion.init_app(app)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'jfif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    
app.register_blueprint(productos)
app.register_blueprint(categorias)
app.register_blueprint(vistas)
