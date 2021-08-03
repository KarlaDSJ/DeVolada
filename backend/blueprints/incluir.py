from main import db
from flask import Blueprint, request, jsonify
from models.compraM import Compra
from models.productoM import Producto
from models.incluirM import Incluir
from pprint import pprint

incluir = Blueprint('incluir', __name__)

@incluir.route('/incluir', methods=['POST'])
def incluir_productos():
    ''' Incluye un producto a una compra con una cantidad
    
    Returns:
    Json indicando si se pudo o no completar la inclusión'''
    producto = request.json['producto']
    compra = request.json['compra']
    cantidad = request.json['cantidad']

    # Checo que no exista
    nueva_inclusion = Incluir.query.get((producto, compra))

    if nueva_inclusion is None:
        nueva_inclusion = Incluir(producto, compra, cantidad)
        db.session.add(nueva_inclusion)
        db.session.commit()
        return jsonify({'msg': 'se incluyó el producto a la compra'})
    else:
        return jsonify({'msg':'No se pudo completar la petición'})
    

