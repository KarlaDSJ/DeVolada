from main import db
from flask import Blueprint, request, jsonify
from models.direccionCompradorM import DireccionComprador
from schemas.direccionCompradorE import DireccionCompradorEsquema
from pprint import pprint

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones para crear una dirección del comprador
"""

direccionComprador = Blueprint('direccionComprador',__name__)

"""---------------- Esquemas ----------------"""

direccionComprador_esquema = DireccionCompradorEsquema()
direccionesComprador_esquema = DireccionCompradorEsquema(many=True)

"""---------------- Rutas ----------------"""

@direccionComprador.route('/direccionComprador/<id_direccionComprador>', methods=['GET'])
def obtener_direccionComprador(id_direccionComprador):  
    '''
    Obtiene la información de una dirección dado su id
    Params:
        id_direccionComprador: identificador de la dirección del comprador
    Returns: 
    Json con la información de la dirección, o un mensaje con error 404 al
    no poder encontrarla
    '''  

    direccionComprador = DireccionComprador.query.get(id_direccionComprador)
    if direccionComprador is None:
        return jsonify({'msg': 'No existe esa direccion'}), 404
    else:
        return direccionComprador_esquema.jsonify(direccionComprador)


# Maaaal. Debe revisar campo por campo para que no haya duplicados
@direccionComprador.route('/direccionComprador', methods=['POST'])
def agrega_direccionComprador(): 
    '''
    Agrega una dirección a un comprador
    Returns:
    Json con un mensaje indicando que se registró, y su identificador. 
    En caso de error, 400 con un mensaje indicando que ya ha sido 
    registrada
    '''

    correo = request.json['correo']
    estado = request.json['estado'] 
    ciudad = request.json['ciudad'] 
    colonia = request.json['colonia'] 
    cp = request.json['cp'] 
    calle = request.json['calle'] 
    numero = request.json['numero']

    dirC = DireccionComprador.query.filter_by(correo=correo, estado=estado, ciudad=ciudad, colonia=colonia, cp=cp, calle=calle, numero=numero).first()
    pprint(dirC)
    if dirC is None:
        dirC = DireccionComprador(correo, estado, ciudad, colonia, cp, calle, numero)
        pprint(dirC)
        db.session.add(dirC)
        db.session.commit()        
        return jsonify({'msg': 'Se registró la dirección', 'idDir': dirC.idDir})
    else:
        return jsonify({'msg': 'Esa dirección ya está registrada'}), 400



@direccionComprador.route('/direccionComprador/direcciones/<correo>', methods=['GET'])
def obtener_direccionesComprador(correo): 
    '''
    Obtiene una lista con todas las direcciones de un comprador
    
    Returns: 
    Lista de todas las direcciones registradas
    '''

    direccionComprador = DireccionComprador.query.filter_by(correo=correo).all()
    return direccionesComprador_esquema.jsonify(direccionComprador)