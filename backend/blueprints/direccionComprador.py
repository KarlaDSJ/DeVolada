from main import db
from flask import Blueprint, request, jsonify
from models.direccionCompradorM import DireccionComprador
from schemas.direccionCompradorE import DireccionCompradorEsquema
from pprint import pprint

direccionComprador = Blueprint('direccionComprador',__name__)

direccionComprador_esquema = DireccionCompradorEsquema()
direccionesComprador_esquema = DireccionCompradorEsquema(many=True)


@direccionComprador.route('/direccionComprador/<id_direccionComprador>', methods=['GET'])
def obtener_direccionComprador(id_direccionComprador):  
    '''Obtiene la información de una dirección dado su id '''  
    direccionComprador = DireccionComprador.query.get(id_direccionComprador)
    if direccionComprador is None:
        return jsonify({'msg': 'No existe esa direccion :('})
    else:
        return direccionComprador_esquema.jsonify(direccionComprador)


# Maaaal. Debe revisar campo por campo para que no haya duplicados
@direccionComprador.route('/direccionComprador', methods=['POST'])
def agrega_direccionComprador(): 
    '''Agrega una dirección a un comprador'''
    correo = request.json['correo']
    estado = request.json['estado'] 
    ciudad = request.json['ciudad'] 
    colonia = request.json['colonia'] 
    cp = request.json['cp'] 
    calle = request.json['calle'] 
    numero = request.json['numero']

    dirC = DireccionComprador.query.filter_by(correo=correo, estado=estado, ciudad=ciudad, colonia=colonia, cp=cp, calle=calle, numero=numero).first()
    if dirC is None:
        dirC = DireccionComprador(correo, estado, ciudad, colonia, cp, calle, numero)
        pprint(dirC)
        db.session.add(dirC)
        db.session.commit()        
        return direccionComprador_esquema.jsonify(dirC)
    else:
        return jsonify({'msg': 'Esa dirección ya está registrada'})



@direccionComprador.route('/direccionComprador/direcciones/<correo>', methods=['GET'])
def obtener_productos_direccionComprador(correo): 
    '''Obtiene una lista con todas las direcciones de un comprador'''

    direccionComprador = DireccionComprador.query.filter_by(correo=correo).all()
    return direccionesComprador_esquema.jsonify(direccionComprador)