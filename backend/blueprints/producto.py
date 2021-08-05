from sqlalchemy import desc, func
from main import db
from flask import Blueprint, request, jsonify
from models.productoM import Producto
from models.categoriaM import Categoria
#from models.incluirM import Incluir
from schemas.productoS import ProductoEsquema

producto = Blueprint('producto', __name__)

"""---------------- Esquemas ----------------"""

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

"""---------------- Rutas ----------------"""
#Falta que regrese el id

@producto.route('/producto/<id>', methods=['GET'])
def get_producto(id):
    """Nos regresa la información del producto con
     imagenes, sin categoría ni reseñas"""
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
    if len(categoria) == 0:
        #buscamos por nombre
        productos = db.session.query(Producto).filter_by(nombre=nombre).all()
    elif len(nombre) == 0:
        #Buscamos por categoria
        productos = db.session.query(Producto).join(Categoria).filter_by(categoria=categoria).all()
    else:
        #Busqueda por nombre y categoria
        productos = db.session.query(Producto).filter_by(nombre=nombre).join(Categoria).filter_by(categoria=categoria).all()
    return productos_esquema.jsonify(productos)

@producto.route('/producto/top5', methods=['GET'])
def top5_productos():
    """Nos regresa los 5 productos más vendidos, si no hay ventas 
    nos regresa los 5 más recientes"""
    ##productos = db.session.query(func.sum(Incluir.cantidad).label('count'), Incluir.producto).group_by(Incluir.producto).order_by(desc('count')).limit(5)
    ##if len(productos) == 0: #Probar que lo de arriba funcione
    productos = db.session.query(Producto).order_by(Producto.idProducto.desc()).limit(5)
    return productos_esquema.jsonify(productos)


"""@producto.route('/producto/<id>', methods=['GET'])
def obtener_producto(id):    
    producto = Producto.query.get(id)
    return jsonify({'vendedor_correo': producto.correo, 'nombre': producto.nombre,
                    'disponibles': producto.disponibles})"""


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