from sqlalchemy import desc, func
from sqlalchemy.sql.functions import count
from main import db
from flask import Blueprint, request, jsonify
from models.productoM import Producto
from models.incluirM import Incluir
from models.categoriaM import Categoria
from schemas.productoS import ProductoEsquema

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones CRUD para un producto
"""

producto = Blueprint('producto', __name__)

"""---------------- Esquemas ----------------"""

producto_esquema = ProductoEsquema()
productos_esquema = ProductoEsquema(many=True)

"""---------------- Rutas ----------------"""

@producto.route('/producto/<id>', methods=['GET'])
def get_producto(id):
    """
    Nos regresa la información del producto con
     imagenes y categorías
    Params:        
        id: identificador del producto
    Returns: lista de los productos
    """

    producto = db.session.query(Producto).filter_by(idProducto=id).first()

    return producto_esquema.jsonify(producto)


@producto.route('/productos', methods=['GET'])
def get_productos():
    """
    Nos regresa todos los productos
    Returns: lista de los productos
    """

    productos = db.session.query(Producto).all()
 
    return productos_esquema.jsonify(productos)


@producto.route('/producto/buscar', methods=['POST'])
def search_productos():
    """
    Nos regresa todos los productos que coincidan 
      con el nombre y categoría
    Params:        
        categoria: categoría a buscar
        nombre: nombre del producto a buscar
    Returns: lista de los productos
    """

    categoria = request.json['categoria']
    nombre = request.json['nombre']
    if len(categoria) == 0:
        #Buscamos por nombre
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
    """
    Nos regresa los 5 productos más vendidos, si no hay ventas 
    nos regresa los 5 más recientes

    Returns: lista de los productos
    """
    productos = db.session.query(Producto).join(Incluir).order_by(desc(Incluir.cantidad)).limit(5)
    if productos.count() == 0: 
        productos = db.session.query(Producto).order_by(Producto.idProducto.desc()).limit(5)
    return productos_esquema.jsonify(productos)


@producto.route('/productos/vendedor/<correo>', methods=['GET'])
def obten_productos_vendedor(correo):
    """
    Obtiene todos los productos de un vendedor

    Params:        
        correo: identificador del vendedor
    Returns: lista de los productos
    """

    productos = db.session.query(Producto).filter_by(correo=correo).all()
    return productos_esquema.jsonify(productos)


@producto.route('/producto', methods=['POST'])
def agrega_producto():    
    """
    Agrega un producto a la base de datos

    Returns: La información del producto agregado
    o un mensaje de error
    """

    correo = request.json['correo']
    nombre = request.json['nombre'].strip()
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    disponibles = request.json['disponibles']

    if (correo == ""):
        return jsonify({"error": 100, "mensaje": "No hay un correo asignado a la petición."})
    if (nombre == ""):
        return jsonify({"error": 101, "mensaje": "El producto debe tener un nombre."})
    if (not (type(precio) == float or type(precio) == int)):
        return jsonify({"error": 103, "mensaje": "El precio del producto debe ser un número."})
    if (precio <= 0):
        return jsonify({"error": 102, "mensaje": "El precio del producto debe ser mayor a cero."})
    if (descripcion == ""):
        return jsonify({"error": 104, "mensaje": "El producto debe tener una descripcion."})
    if (type(disponibles) != int):
        return jsonify({"error": 105, "mensaje": "La cantidad de unidades disponibles debe ser un número entero."})
    if (disponibles <= 0):
        return jsonify({"error": 106, "mensaje": "La cantidad de unidades disponibles debe ser mayor a cero."})

    producto_nuevo = Producto(correo, precio, nombre, descripcion, 0, disponibles)

    db.session.add(producto_nuevo)
    db.session.commit()

    return producto_esquema.jsonify(producto_nuevo)


@producto.route('/producto/<id>', methods=['PATCH'])
def actualiza_producto(id):    
    """
    Actualiza la información de un producto

    Params:        
        id: identificador deproducto
    Returns: información actualizada del producto 
    o un mensaje de error
    """

    producto = db.session.query(Producto).filter_by(idProducto=id).first()

    if (producto is None):
        return jsonify({"mensaje": "No se puedo actualizar el producto <" + id + "> porque no existe."})

    json_dict = request.get_json(force=True)
    if 'nombre' in json_dict:
        producto.nombre  = request.json['nombre']
    if 'precio' in json_dict:
        producto.precio  = request.json['precio']
    if 'descripcion' in json_dict:
        producto.descripcion  = request.json['descripcion']
    if 'disponibles' in json_dict:
        producto.disponibles  = request.json['disponibles']   

    db.session.commit()
    return producto_esquema.jsonify(producto)


@producto.route('/producto/<id>', methods=['DELETE'])
def elimina_producto(id):  
    """
    Elimina un producto de la base de datos

    Params:        
        id: identificador deproducto
    Returns: mensaje de éxito o de error
    """  
    producto_eliminar = db.session.query(Producto).filter_by(idProducto=id).first()

    if (producto is None):
        return jsonify({"error": 101, "mensaje": "No se puedo eliminar el producto <" + id + "> porque no existe."})

    db.session.delete(producto_eliminar)
    db.session.commit()
    return jsonify({"mensaje": "Se elimino el producto <" + id + "> correctamente"})

