from main import db
from flask import Blueprint, request, jsonify
from models.contenerM import Contener
from models.productoM import Producto
from schemas.contenerE import ContenerEsquema
from schemas.productoS import ProductoEsquema

contener = Blueprint('contener',__name__)

contener_esquema = ContenerEsquema()
conteneres_esquema = ContenerEsquema(many=True)


@contener.route('/contener', methods=['POST'])
def agregar_producto():    
    idProducto = request.json['idProducto']
    idCarrito = request.json['idCarrito']
    cantidad = 1

    contener_nuevo = Contener(idProducto, idCarrito, cantidad)

    db.session.add(contener_nuevo)
    db.session.commit()

    return contener_esquema.jsonify(contener_nuevo)

@contener.route('/contener', methods=['PUT'])
def actualizar_cantidad():    
    idProducto = request.args.get('idProducto', '')  
    idCarrito = request.args.get('idCarrito', '') 

    cantidad = request.json['cantidad'] 
    contener = Contener.query.get((idProducto, idCarrito))
    disponibles = Producto.query.get(idProducto).disponibles

    if (disponibles>=cantidad):
        contener.cantidad = cantidad
        db.session.commit()
        return contener_esquema.jsonify(contener)
    else:
        return jsonify({'msg': 'No se puede aumentar la cantidad'})


@contener.route('/contener', methods=['DELETE'])
def borrar_productos():          
    idCarrito = request.args.get('idCarrito', '') 
    # Obtener todos los productos que tiene el carrito 
    productos = Contener.query.filter_by(idCarrito=idCarrito).first()

    return contener_esquema.jsonify(productos)