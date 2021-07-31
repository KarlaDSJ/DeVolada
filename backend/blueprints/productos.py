from main import db
from flask import Blueprint, request, jsonify
from models.productoM import Producto
from schemas.productoS import ProductoEsquema


producto = Blueprint('producto', __name__)

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

@producto.route('/producto', methods=['GET'])
def get():
    return jsonify ({'msg': 'Bienvenido a DeVolada'})

@producto.route('/producto', methods=['POST'])
def agrega_producto():
    correo = request.json['correo']
    precio = request.json['precio']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    vendidos = request.json['vendidos']
    disponible = request.json['disponible']

    producto_nuevo = Producto(correo, precio, nombre, descripcion, vendidos, disponible)

    db.session.add(producto_nuevo)
    db.session.commit()

    return producto_esquema.jsonify(producto_nuevo)