from main import db
from flask import Blueprint, request, jsonify
from models.compraM import Compra
from models.productoM import Producto
from models.incluirM import Incluir
from models.productoM import Producto
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
Archivo de rutas para poder manejar las peticiones para crear la relación incluir entre compra y producto
"""
incluir = Blueprint('incluir', __name__)

@incluir.route('/incluir', methods=['POST'])
def incluir_productos():
    ''' 
    Incluye un producto a una compra con una cantidad
    
    Returns:
    Json indicando si se pudo o no completar la inclusión
    En caso de que no se produce el error 400
    '''
    
    producto = request.json['producto']
    compra = request.json['compra']
    cantidad = request.json['cantidad']

    # Checo que no exista
    nueva_inclusion = Incluir.query.get((producto, compra))

    if nueva_inclusion is None:
        nueva_inclusion = Incluir(producto, compra, cantidad)
        Producto.query.get(producto).vendidos += cantidad
        Producto.query.get(producto).disponibles -= cantidad
        db.session.add(nueva_inclusion)
        db.session.commit()
        return jsonify({'msg': 'se incluyó el producto a la compra'})
    else:
        return jsonify({'msg':'No se pudo completar la petición'}), 400
    

