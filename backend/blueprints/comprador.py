from main import db # importamos la instanica de la base de datos
from flask import Blueprint, request, jsonify # para poder hacer los JSON
from models.compradorM import Comprador # el modelo del Comprador
from schemas.compradorE import CompradorEsquema # el schema del Comprador

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones sobre el comprador
"""

# Inicializamos el blueprint

comprador = Blueprint('comprador',__name__)

"""---------------- Esquemas ----------------"""
# Instnaciamos los eschemas

comprador_esquema = CompradorEsquema()
compradores_esquema = CompradorEsquema(many=True)

"""---------------- Rutas ----------------"""

@comprador.route('/comprador/<correo>', methods=['GET'])
def obtener_comprador(correo):    
    """ 
    Metodo para obtener los datos del comprador segun su id
    Params:        
        correo: identificador del comprador
    Returns: un JSON con los datos del comprador
    """

    comprador = Comprador.query.get(correo)
    return comprador_esquema.jsonify(comprador)


@comprador.route('/comprador', methods=['POST'])
def agrega_comprador():
    """
    Metodo para agregar un nuevo comprador
    Returns: un JSON con los datos del nuevo comprador 
    """

    correo = request.json['correo']
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    contrasenia = request.json['contrasenia']

    comprador_nuevo = Comprador(correo, nombre, telefono, contrasenia)

    db.session.add(comprador_nuevo)
    db.session.commit()

    return comprador_esquema.jsonify(comprador_nuevo)