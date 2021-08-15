from main import db
from flask import Blueprint, request, jsonify
from models.carritoM import Carrito
from schemas.carritoE import CarritoEsquema

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones sobre el carrito
"""

carrito = Blueprint('carrito', __name__)

"""---------------- Esquemas ----------------"""

carrito_esquema = CarritoEsquema()
carritos_esquema = CarritoEsquema(many=True)

"""---------------- Rutas ----------------"""

@carrito.route('/carrito', methods=['POST'])
def agrega_carrito():
    """
    Crea un carrito de compras
    
    Returns: identificador del carrito y una lista vacía
    indicando que no tiene productos en él
    """
    
    carrito_nuevo = Carrito()
    db.session.add(carrito_nuevo)
    db.session.commit()
    return carrito_esquema.jsonify(carrito_nuevo)


@carrito.route('/carrito/<id_carrito>/productos', methods=['GET'])
def obtener_productos_carrito(id_carrito):
    """
    Obtiene los productos de un carrito
    Params:        
        id_carrito: identificador del carrito
    Returns: lista de identificadores de los productos que
    contiene el carrito, además del identificador del mismo
    """

    carrito = Carrito.query.get(id_carrito)
    if carrito is None:
        return jsonify({'msg': 'No existe el carrito :('})
    else:
        return carrito_esquema.jsonify(carrito)
