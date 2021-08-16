from main import db
from flask import Blueprint, request, jsonify
from models.contenerM import Contener
from models.productoM import Producto
from schemas.contenerE import ContenerEsquema
from schemas.productoS import ProductoEsquema
from pprint import pprint

from marshmallow import Schema, fields

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones sobre la tabla contener
"""

contener = Blueprint('contener', __name__)

"""---------------- Esquemas ----------------"""

contener_esquema = ContenerEsquema()
conteneres_esquema = ContenerEsquema(
    only=("idProducto", "cantidad"), many=True)

"""---------------- Rutas ----------------"""

@contener.route('/contener', methods=['POST'])
def agregar_producto():
    '''
    Crea una relación contener entre un carrito y un producto.
    Ambos son pasados en el cuerpo como  "idProducto" y "idCarrito".
    Si ya existe la relación intenta aumentar la cantidad.
    
    Returns:
    Un mensaje en formato json indicando si se agregó o no. 
    '''

    idProducto = request.json['idProducto']
    idCarrito = request.json['idCarrito']
    cantidad = 1

    contener_nuevo = Contener.query.get((idProducto, idCarrito))

    if contener_nuevo is None:
        contener_nuevo = Contener(idProducto, idCarrito, cantidad)
        db.session.add(contener_nuevo)
        db.session.commit()
        return jsonify({'msg': 'Se agregó al carrito'})
    else: 
        disponibles = Producto.query.get(idProducto).disponibles
        cantidad = contener_nuevo.cantidad +1

        if (disponibles >= cantidad):
            contener_nuevo.cantidad = cantidad
            db.session.commit()
            return jsonify({'msg': 'Se agregó al carrito'})
        else:
            return jsonify({'msg': 'Ya no hay más productos disponibles'}), 400


@contener.route('/contener', methods=['PUT'])
def actualizar_cantidad():
    '''
    Actualiza la cantidad de un producto en un carrito.
    Ambos parámetros de la ruta, "idCarrito" y "idProducto".
    La cantidad se pide en un json con "cantidad".
    
    Returns:
    En ambos casos un json con la información de la
    relación. En caso de no poder aumentar la cantidad la deja
    cómo estaba
    '''


    idProducto = request.args.get('idProducto', '')
    idCarrito = request.args.get('idCarrito', '')

    cantidad = request.json['cantidad']
    contener = Contener.query.get((idProducto, idCarrito))

    disponibles = Producto.query.get(idProducto).disponibles

    if (disponibles >= cantidad):
        contener.cantidad = cantidad
        db.session.commit()
    
    return contener_esquema.jsonify(contener)
           


@contener.route('/contener', methods=['GET'])
def productos_en_el_carrito():
    '''
    Obtiene todos los productos del carrito.
    Necesita el id del carrito por parámetro de 
    ruta "idCarrito".

    Returns:
    Lista de formatos json con la información requerida.
    '''

    idCarrito = request.args.get('idCarrito', '')
    productos = Contener.query.filter_by(idCarrito=idCarrito).all()

    producto_esquema = ProductoEsquema(
        only=("idProducto", "precio", "nombre", "disponibles", "imagenes"))

    datos = conteneres_esquema.dump(productos)
    
    for item in datos:
        x = item.pop('idProducto')
        prod = Producto.query.get(x)
        informacion = producto_esquema.dump(prod)
        item.update(informacion)

    return jsonify(datos)


@contener.route('/totalCarrito', methods=['GET'])
def obtener_total ():
    '''
    Obtiene la suma del precio de los productos
    agregados a un carrito

    Params:        
        idCarrito: identificador del carrito
    Returns:
    Total del carrito.
    '''

    idCarrito = request.args.get('idCarrito', '')
    productos = Contener.query.filter_by(idCarrito=idCarrito).all()

    datos = conteneres_esquema.dump(productos)
    total = 0
    for item in datos:
        x = item.pop('idProducto')
        prod = Producto.query.get(x) 
        total+= prod.precio * item.pop('cantidad')

    return jsonify(total)


@contener.route('/contener', methods=['DELETE'])
def eliminar_producto():
    '''
    Elimina el producto del carrito, ambos son parámetros 
    de la ruta. "idCarrito" y "idProducto". 
    
    Returns:
    Mensaje en formato json indicando si se pudo eliminar o no.
    '''

    idCarrito = request.args.get('idCarrito', '')
    idProducto = request.args.get('idProducto', '')
    
    try:
        producto = Contener.query.get((idProducto, idCarrito))
        db.session.delete(producto)
        db.session.commit()
        return jsonify({'msg': 'Se eliminó del carrito'})
    except Exception as e:
        return jsonify({'msg': 'Hubo un error'})




@contener.route('/limpiarCarrito', methods=['DELETE'])
def limpiar_carrito():
    '''
    Limpia el carrito del que se le pasa el id en la ruta
    como "idCarrito".
    
    Returns:
    Mensaje en formato json indicando si se pudo limpiar o no.
    '''
    
    idCarrito = request.args.get('idCarrito', '')

    productos = Contener.query.filter_by(idCarrito=idCarrito)
    conteneres_esquema = ContenerEsquema(
        only=("idProducto", "idCarrito"), many=True)
    datos = conteneres_esquema.dump(productos)

    try:
        for item in datos:
            id_producto = item['idProducto']
            id_carrito = item['idCarrito']
            producto = Contener.query.get((id_producto, id_carrito))            
            db.session.delete(producto)
            db.session.commit()
        return jsonify({'msg': 'Se limpió el carrito'})
    except Exception as e:
        return jsonify({'msg': 'Hubo un error'})