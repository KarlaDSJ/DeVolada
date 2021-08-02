from main import db
from flask import Blueprint, request, jsonify
from models.productoM import Producto
from schemas.productoS import ProductoEsquema

producto = Blueprint('producto',__name__)

producto_esquema = ProductoEsquema()
productoes_esquema = ProductoEsquema(many=True)

@producto.route('/producto/<id>', methods=['GET'])
def obtener_producto(id):    
    producto = Producto.query.get(id)
    return jsonify({'vendedor_correo': producto.correo, 'nombre': producto.nombre,
                    'disponibles': producto.disponibles})


@producto.route('/producto', methods=['POST'])
def agrega_producto():    
    correo = request.json['correo']
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    vendidos = request.json['vendidos']
    disponibles = request.json['disponibles']

    producto_nuevo = Producto(correo, precio, nombre, descripcion, vendidos, disponibles)

    db.session.add(producto_nuevo)
    db.session.commit()

    return producto_esquema.jsonify(producto_nuevo)