from main import db
from flask import Blueprint, request, jsonify
from models.tarjetaCompradorM import TarjetaComprador
from schemas.tarjetaCompradorE import TarjetaEsquema

from marshmallow import Schema, fields
# from pprint import pprint

tarjetaComprador = Blueprint('tarjetaComprador', __name__)

tarjetaComprador_esquema = TarjetaEsquema()
tarjetaCompradores_esquema = TarjetaEsquema( many=True)


@tarjetaComprador.route('/tarjetaComprador', methods=['POST'])
def agregar_producto():

    correo = request.args.get('correo', '')
    numero = request.json['numero']
    cvv = request.json['cvv']
    duenio = request.json['duenio']
    fechaCad = request.json['fechaCad']
    cantidad = 1

    tarjetaComprador_nuevo = Tarjeta.query.get((idProducto, idCarrito))

    if tarjetaComprador_nuevo is None:
        tarjetaComprador_nuevo = Tarjeta(idProducto, idCarrito, cantidad)
        db.session.add(tarjetaComprador_nuevo)
        db.session.commit()
        return jsonify({'msg': 'Se agregó al carrito'})
    else: 
        disponibles = Producto.query.get(idProducto).disponibles
        cantidad = tarjetaComprador_nuevo.cantidad +1

        if (disponibles >= cantidad):
            tarjetaComprador_nuevo.cantidad = cantidad
            db.session.commit()
            return jsonify({'msg': 'Se agregó al carrito'})
        else:
            return jsonify({'msg': 'No se puede agregar al carrito'})


# @tarjetaComprador.route('/tarjetaComprador', methods=['PUT'])
# def actualizar_cantidad():
#     '''Actualiza la cantidad de un producto en un carrito.
#     Ambos parámetros de la ruta, "idCarrito" y "idProducto".
#     La cantidad se pide en un json con "cantidad".
    
#     Returns:
#     En ambos casos un json con la información de la
#     relación. En caso de no poder aumentar la cantidad la deja
#     cómo estaba'''

#     idProducto = request.args.get('idProducto', '')
#     idCarrito = request.args.get('idCarrito', '')

#     cantidad = request.json['cantidad']
#     tarjetaComprador = Tarjeta.query.get((idProducto, idCarrito))
#     disponibles = Producto.query.get(idProducto).disponibles

#     if (disponibles >= cantidad):
#         tarjetaComprador.cantidad = cantidad
#         db.session.commit()
    
#     return tarjetaComprador_esquema.jsonify(tarjetaComprador)
           


# @tarjetaComprador.route('/tarjetaComprador', methods=['GET'])
# def productos_en_el_carrito():
#     '''Obtiene todos los productos del carrito.
#     Necesita el id del carrito por parámetro de 
#     ruta "idCarrito".

#     Returns:
#     Lista de formatos json con la información requerida.
#     '''

#     idCarrito = request.args.get('idCarrito', '')
#     productos = Tarjeta.query.filter_by(idCarrito=idCarrito).all()

#     producto_esquema = ProductoEsquema(
#         only=('idProducto', 'precio', 'nombre', 'disponibles'))

#     datos = tarjetaCompradores_esquema.dump(productos)

#     # Aún falta unirlo con las imágenes
#     for item in datos:
#         x = item.pop('idProducto')
#         prod = Producto.query.get(x)
#         informacion = producto_esquema.dump(prod)
#         item.update(informacion)

#     return jsonify(datos)


# @tarjetaComprador.route('/tarjetaComprador', methods=['DELETE'])
# def eliminar_producto():
#     '''Elimina el producto del carrito, ambos parámetros de la ruta
#     "idCarrito" y "idProducto".
    
#     Returns:
#     Mensaje en formato json indicando si se pudo eliminar o no.'''

#     idCarrito = request.args.get('idCarrito', '')
#     idProducto = request.args.get('idProducto', '')
    
#     try:
#         producto = Tarjeta.query.get((idProducto, idCarrito))
#         db.session.delete(producto)
#         db.session.commit()
#         return jsonify({'msg': 'Se eliminó del carrito'})
#     except Exception as e:
#         return jsonify({'msg': 'Hubo un error'})




# @tarjetaComprador.route('/tarjetaComprador', methods=['DELETE'])
# def limpiar_carrito():
#     '''Limpia el carrito del que se le pasa el id en la ruta
#     como "idCarrito".
    
#     Returns:
#     Mensaje en formato json indicando si se pudo limpiar o no.'''

#     idCarrito = request.args.get('idCarrito', '')

#     productos = Tarjeta.query.filter_by(idCarrito=idCarrito)
#     tarjetaCompradores_esquema = TarjetaEsquema(
#         only=("idProducto", "idCarrito"), many=True)
#     datos = tarjetaCompradores_esquema.dump(productos)

#     try:
#         for item in datos:
#             id_producto = item['idProducto']
#             id_carrito = item['idCarrito']
#             producto = Tarjeta.query.get((id_producto, id_carrito))
#             db.session.delete(producto)
#             db.session.commit()
#         return jsonify({'msg': 'Se limpió el carrito'})
#     except Exception as e:
#         return jsonify({'msg': 'Hubo un error'})