from main import db
from flask import Blueprint, request, jsonify
from models.carritoM import Carrito
from schemas.carritoE import CarritoEsquema

carrito = Blueprint('carrito', __name__)

carrito_esquema = CarritoEsquema()
carritos_esquema = CarritoEsquema(many=True)

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
