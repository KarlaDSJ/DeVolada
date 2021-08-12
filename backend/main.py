from flask import Flask  #bibliotecas de flask
from flask_cors import CORS #bibliotes de cors
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_mail import Mail

""" 
Primero se crean dos instancias de SQLAlchemy y de Mashmellow fuentes:
https://www.sqlalchemy.org/
https://marshmallow.readthedocs.io/en/stable/

SQLAlchemy es una aplcación para mapear Bases de Datos relacionales para SQL
Marshmallow es un ORM o framework para convertir tipos de datos y serializarlos 
"""

db = SQLAlchemy()
ma = Marshmallow()

from flask_wtf.csrf import CSRFProtect # para cifrar datos
from config import DevelopmentConfig # para la configuración de la aplicación

"""
Blueprint
Se implementa los blueprint para que el funcionamiento de flask
se reparta en distintos archivos
"""

from blueprints.logout import logout
from blueprints.create import create
from blueprints.login import login
from blueprints.index import index
from blueprints.producto import producto
from blueprints.comprador import comprador
from blueprints.vendedor import vendedor
from blueprints.imagen import imagen
from blueprints.categoria import categoria
from blueprints.direccionVendedor import direccionVendedor
from blueprints.carrito import carrito
from blueprints.pertenecer import pertenecer
from blueprints.contener import contener
from blueprints.direccionComprador import direccionComprador
from blueprints.tarjetaComprador import tarjetaComprador
from blueprints.compra import compra
from blueprints.incluir import incluir
from blueprints.resena import resena

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@cienncias.unam.mx"
__status__ = "Development"

# Iniciamos una instanica de Flask

app = Flask(__name__)

# Iniciamos una instancia de CSRF para cifrar los datos 

csrf = CSRFProtect()

""" 
Los CORS (Intecambio de Recursos de Origen Cruzado) sirven para que el front end pueda concetarse con el backend,
pues el front end se encuetra en un dominio distinto a del backend,
en resumen es como un "permiso"
"""

CORS(app)

# Utlizamos la configuración de la app que esta en el archivo config.py

app.config.from_object(DevelopmentConfig)

# Configuramos una isntancia de Meil para poder mandar correos

mail = Mail()

mail.init_app(app)

app.register_blueprint(comprador)
app.register_blueprint(vendedor)
app.register_blueprint(producto)
app.register_blueprint(imagen)
app.register_blueprint(categoria)
app.register_blueprint(direccionVendedor)
app.register_blueprint(carrito)
app.register_blueprint(resena)
app.register_blueprint(login)
app.register_blueprint(index)
app.register_blueprint(create)
app.register_blueprint(logout)
app.register_blueprint(pertenecer)
app.register_blueprint(contener)
app.register_blueprint(direccionComprador)
app.register_blueprint(tarjetaComprador)
app.register_blueprint(compra)
app.register_blueprint(incluir)

# Iniciamos la app con la base de datos

db.init_app(app)

# solo es por si se compila main.py aunque podrá generar errores y busgs

if __name__ == '__main__':
    app.run(port=7000)    
    
    with app.app_context():
        db.create_all()
        ma.init_app(app)

    
