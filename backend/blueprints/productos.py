from sqlalchemy import desc, func
from main import db
from flask import Blueprint, request, jsonify
from models.productoM import Producto
#from models.incluirM import Incluir
from schemas.productoS import ProductoEsquema
from schemas.imagenS import ImagenEsquema

producto = Blueprint('producto', __name__)

"""---------------- Esquemas ----------------"""

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)
foto_esquema = ImagenEsquema()
fotos_esquema = ImagenEsquema(many=True)

"""---------------- Rutas ----------------"""
#Falta que el producto jale las fotos y la categoría 
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

#Hay que modificar la query si nos mandan una categoría
@producto.route('/producto/buscar', methods=['GET'])
def search_productos():
    """Nos regresa todos los productos que coincidan 
      con el nombre y categoría"""
    categoria = request.json['categoria']
    nombre = request.json['nombre']

    productos = db.session.query(Producto).filter_by(nombre=nombre).all()
    return productos_esquema.jsonify(productos)

@producto.route('/producto/top5', methods=['GET'])
def top5_productos():
    """Nos regresa los 5 productos más vendidos, si no hay ventas 
    nos regresa los 5 más recientes"""
    ##productos = db.session.query(func.sum(Incluir.cantidad).label('count'), Incluir.producto).group_by(Incluir.producto).order_by(desc('count')).limit(5)
    ##if len(productos) == 0: #Probar que lo de arriba funcione
    productos = db.session.query(Producto).order_by(Producto.idProducto.desc()).limit(5)
    return productos_esquema.jsonify(productos)