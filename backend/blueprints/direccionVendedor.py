from main import db
from flask import Blueprint, request, jsonify
from models.direccionVendedorM import DireccionVendedor
from schemas.direccionE import DireccionEsquema

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones para crear una dirección del vendedor
"""

direccionVendedor = Blueprint('direccionVendedor', __name__)

"""---------------- Esquemas ----------------"""

direccionVendedor_esquema = DireccionEsquema()

"""---------------- Rutas ----------------"""

@direccionVendedor.route('/direccion/vendedor', methods=['POST'])
def agrega_direccion():
    '''
    Agregar una direccion de vendedor a la base de datos
    Returns:
    Json con l ainformación de la dirección o  un mensaje de error 
    '''

    correo  = request.json['correo']
    estado  = request.json['estado']
    ciudad  = request.json['ciudad']
    colonia = request.json['colonia']
    cp      = request.json['cp']
    calle   = request.json['calle']
    numero  = request.json['numero']

    direccion = db.session.query(DireccionVendedor).filter_by(correo=correo).first()
    if (direccion is not None):
        return jsonify({"mensaje:": "No se pudo agregar. El vendedor <" + correo + "> ya tiene una dirección registrada."})
    
    direccion_nueva = DireccionVendedor(correo, estado, ciudad, colonia, cp, calle, numero)
    db.session.add(direccion_nueva)
    db.session.commit()
    return direccionVendedor_esquema.jsonify(direccion_nueva) 


@direccionVendedor.route('/direccion/vendedor', methods=['GET'] )
def obten_direccion():
    '''
    Obtiene la direccion del vendedor en la base de datos
    
    Returns: 
    La dirección registrada
    '''

    correo  = request.json['correo']
    direccion = db.session.query(DireccionVendedor).filter_by(correo=correo).first()
    return direccionVendedor_esquema.jsonify(direccion)


@direccionVendedor.route('/direccion/vendedor', methods=['PATCH'])
def actualiza_direccion():
    '''
    Actualiza la direccion del vendedor en la base de datos
    
    Returns: 
    La dirección actualizada
    '''

    correo  = request.json['correo']
    json_dict = request.get_json(force=True)
    direccion = db.session.query(DireccionVendedor).filter_by(correo=correo).first()

    if (direccion is  None):
        return jsonify({"mensaje:": "No se pudo modificar. El vendedor <" + correo + "> no tiene una direccion registrada."})

    if 'ciudad' in json_dict:
        direccion.ciudad  = request.json['ciudad']
    if 'colonia' in json_dict:
        direccion.colonia  = request.json['colonia']
    if 'cp' in json_dict:
        direccion.cp  = request.json['cp']
    if 'calle' in json_dict:
        direccion.calle  = request.json['calle']
    if 'numero' in json_dict:
        direccion.numero  = request.json['numero']
    if 'estado' in json_dict:
        direccion.estado  = request.json['estado']

    return direccionVendedor_esquema.jsonify(direccion)

