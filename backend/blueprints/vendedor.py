from main import db
from flask import Blueprint, request, jsonify
from models.vendedorM import Vendedor
from schemas.vendedorE import VendedorEsquema
from pprint import pprint

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones para obtener la información de un vendedor
"""

vendedor = Blueprint('vendedor',__name__)

"""---------------- Esquemas ----------------"""

vendedor_esquema = VendedorEsquema()
vendedores_esquema = VendedorEsquema(many=True)

"""---------------- Rutas ----------------"""

@vendedor.route('/vendedor/<correo>', methods=['GET'])
def obtener_vendedor(correo):
    """ 
    Metodo para obtener los datos del vendedor segun su id
    Params:        
        correo: identificador del vendedor
    Returns: un JSON con los datos del comprador
    """

    vendedor = Vendedor.query.get(correo)
    pprint(vendedor)
    return jsonify({'correo': vendedor.correo, 'nombre': vendedor.nombre,
                    'telefono': vendedor.telefono})


@vendedor.route('/vendedor', methods=['POST'])
def agrega_vendedor():
    """
    Metodo para agregar un nuevo vendedor
    Returns: un JSON con los datos del nuevo vendedor
    """

    correo = request.json['correo']
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    contrasenia = request.json['contrasenia']

    vendedor_nuevo = Vendedor(correo, nombre, telefono, contrasenia)

    db.session.add(vendedor_nuevo)
    db.session.commit()

    return vendedor_esquema.jsonify(vendedor_nuevo)