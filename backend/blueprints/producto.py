from sqlalchemy import desc, func
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import count
from main import db
from flask import Blueprint, request, jsonify
from models.productoM import Producto
from models.incluirM import Incluir
from models.categoriaM import Categoria
from schemas.productoS import ProductoEsquema
from schemas.imagenE import ImagenEsquema
import os
import base64

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
    descripcion = request.json['descripcion'].strip()
    disponibles = request.json['disponibles']

    # Valida que los datos recibidos sean correctos
    validacion = valida_datos(correo,nombre,precio,descripcion,disponibles)
    if(not validacion["correcto"]): return jsonify(validacion)

    # Agrega el producto a la BD
    producto_nuevo = Producto(correo, precio, nombre, descripcion, 0, disponibles)
    db.session.add(producto_nuevo)
    db.session.commit()

    # Guarda los cambios en la BD
    return producto_esquema.jsonify(producto_nuevo)


@producto.route('/producto/<idProducto>', methods=['PATCH'])
def actualiza_producto(idProducto):
    """
    Actualiza la información de un producto

    Params:        
        id: identificador deproducto
    Returns: información actualizada del producto 
    o un mensaje de error
    """    
    producto = db.session.query(Producto).filter_by(idProducto=idProducto).first()
    correo = request.json['correo']
    nombre = request.json['nombre'].strip()
    precio = request.json['precio']
    descripcion = request.json['descripcion'].strip()
    disponibles = request.json['disponibles']

    # Verifica que el producto exista en la BD
    if (producto is None):
        return jsonify({"error": 100, "mensaje": "El producto <" + str(idProducto) + "> no existe."})

    # Verifica que los datos recibidos sean correctos
    validacion = valida_datos(correo,nombre,precio,descripcion,disponibles)
    if(not validacion["correcto"]): return jsonify(validacion)

    # Actualiza los valores del producto
    producto.nombre  = request.json['nombre']
    producto.precio  = request.json['precio']
    producto.descripcion  = request.json['descripcion']
    producto.disponibles  = request.json['disponibles']   

    # Guarda los cambios en la BD
    db.session.commit()
    return producto_esquema.jsonify(producto)


@producto.route('/producto/<idProducto>', methods=['DELETE'])
def elimina_producto(idProducto):  
    """
    Elimina un producto de la base de datos

    Params:        
        id: identificador deproducto
    Returns: mensaje de éxito o de error
    """  

    producto_eliminar = db.session.query(Producto).filter_by(idProducto=idProducto).first()

    # Verifica que el producto exista en la BD
    if (producto is None):
        return jsonify({"error": 100, "mensaje": "El producto <" + str(idProducto) + "> no existe."})

    # Borra el producto de la BD
    db.session.delete(producto_eliminar)

    # Guarda los cambios en la BDs
    db.session.commit()

    return jsonify({"mensaje": "Se eliminó el producto <" + str(idProducto) + "> correctamente"})


# Verifica que los campos recibidos sean correctos. En caso de fallar
# regresa un json con el mensaje de error.
def valida_datos(correo,nombre,precio,descripcion,disponibles):
    if (correo == ""):
        return {"correcto": False, "error": 101, "mensaje": "No hay un correo asignado a la petición."}
    if (nombre.strip() == ""):
        return {"correcto": False, "error": 102, "mensaje": "El producto debe tener un nombre."}
    if (not (type(precio) == float or type(precio) == int)):
        return {"correcto": False, "error": 103, "mensaje": "El precio del producto debe ser un número."}
    if (precio <= 0):
        return {"correcto": False, "error": 104, "mensaje": "El precio del producto debe ser mayor a cero."}
    if (descripcion.strip() == ""):
        return {"correcto": False, "error": 105, "mensaje": "El producto debe tener una descripcion."}
    if (type(disponibles) != int):
        return {"correcto": False, "error": 106, "mensaje": "La cantidad de unidades disponibles debe ser un número entero."}
    if (disponibles <= 0):
        return {"correcto": False, "error": 107, "mensaje": "La cantidad de unidades disponibles debe ser mayor a cero."}
    return {"correcto": True}
