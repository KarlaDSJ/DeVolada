from sqlalchemy.sql.operators import desc_op
from main import db
from flask import Blueprint, request, jsonify
from models.productoM import Producto
from schemas.productoS import ProductoEsquema
from marshmallow import pprint

producto = Blueprint('producto', __name__)

"""---------------- Esquemas ----------------"""

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

"""---------------- Rutas ----------------"""
#Falta arreglar el esquema para las imagenes
#Verificar que funcionen
#top 5 de productos

##Falta hacer los datos con mokaroo

@producto.route('/producto/id', methods=['GET'])
def get_producto():
    """Nos regresa la información del producto con
     imagenes, sin categoría ni reseñas"""
    id = request.json['id']
    producto = db.session.query(Producto).filter_by(idProducto=id).first()

    return producto_esquema.jsonify(producto)

@producto.route('/productos', methods=['GET'])
def get_productos():
    """Nos regresa todos los productos"""
    productos = db.session.query(Producto).all()

    return productos_esquema.jsonify(productos)

@producto.route('/producto/buscar', methods=['GET'])
def search_productos():
    """Nos regresa todos los productos que coincidan 
      con el nombre y categoría"""
    categoria = request.json['categoria']
    nombre = request.json['nombre']

    productos = db.session.query(Producto).filter_by(nombre=nombre).all()
    return productos_esquema.jsonify(productos)