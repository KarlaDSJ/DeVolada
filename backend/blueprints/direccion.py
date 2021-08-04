from main import db
from flask import Blueprint, request, jsonify
from models.direccionCompradorM import DireccionComprador
from models.direccionVendedorM import DireccionVendedor
from schemas.direccionE import DireccionEsquema


direccion = Blueprint('direccion', __name__)

direccion_esquema = DireccionEsquema()
categoria_esquema = DireccionEsquema(many=True)


# Petición para agregar una direccion de vendedor/comprador a la base de datos.
@direccion.route('/direccion/vendedor', methods=['POST'], defaults={'_tipo_usuario': 'vendedor'})
@direccion.route('/direccion/comprador', methods=['POST'], defaults={'_tipo_usuario': 'comprador'})
def agrega_direccion(_tipo_usuario):
    correo  = request.json['correo']
    estado  = request.json['estado']
    ciudad  = request.json['ciudad']
    colonia = request.json['colonia']
    cp      = request.json['cp']
    calle   = request.json['calle']
    numero  = request.json['numero']

    if (_tipo_usuario == 'vendedor'):
        direccion = db.session.query(DireccionVendedor).filter_by(correo=correo).first()
        if (direccion is not None):
            return jsonify({"mensaje:": "No se pudo agregar. El vendedor <" + correo + "> ya tenia una dirección previamente registrada."})
        direccion_nueva = DireccionVendedor(correo, estado, ciudad, colonia, cp, calle, numero)
        
    
    if (_tipo_usuario == 'comprador'):
        direccion_nueva = DireccionComprador(correo, estado, ciudad, colonia, cp, calle, numero)

    db.session.add(direccion_nueva)
    db.session.commit()
    return direccion_esquema.jsonify(direccion_nueva) 


# Petición para obtener las direcciones de vendedor/comprador de la base de datos.
@direccion.route('/direccion/vendedor', methods=['GET'], defaults={'_tipo_usuario': 'vendedor'})
@direccion.route('/direccion/comprador', methods=['GET'], defaults={'_tipo_usuario': 'comprador'})
def obten_direccion(_tipo_usuario):
    correo  = request.json['correo']

    if (_tipo_usuario == 'vendedor'):
        direccion_usuario = db.session.query(DireccionVendedor).filter_by(correo=correo).first()
    
    if (_tipo_usuario == 'comprador'):
        direccion_usuario = db.session.query(DireccionComprador).filter_by(correo=correo)

    return direccion_esquema.jsonify(direccion_usuario)

'''
# Petición para actualizar las direcciones de vendedor/comprador de la base de datos.
@direccion.route('/direccion/vendedor', methods=['PATCH'], defaults={'_tipo_usuario': 'vendedor'})
@direccion.route('/direccion/comprador', methods=['PATCH'], defaults={'_tipo_usuario': 'comprador'})
def obten_direccion(_tipo_usuario):
    idDir  = request.json['idDir']
    correo  = request.json['correo']
    json_dict = request.get_json(force=True)

    if (_tipo_usuario == 'vendedor'):
        direccion = db.session.query(DireccionVendedor).get((idDir,correo))
    
    if (_tipo_usuario == 'comprador'):
        direccion = db.session.query(DireccionComprador).get((idDir,correo))

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

    return direccion_esquema.jsonify(direccion)
'''

'''
# Petición para eliminar una direccion de vendedor/comprador de la base de datos.
@direccion.route('/direccion/vendedor', methods=['DELETE'], defaults={'_tipo_usuario': 'vendedor'})
@direccion.route('/direccion/comprador', methods=['DELETE'], defaults={'_tipo_usuario': 'comprador'})
def elimina_direccion(_tipo_usuario):
    idDir   = request.json['idDir']
    correo  = request.json['correo']

    if (_tipo_usuario == 'vendedor'):
        direccion_usuario = db.session.query(DireccionVendedor).filter_by(correo=correo).first()
    
    if (_tipo_usuario == 'comprador'):
        direccion_usuario = db.session.query(DireccionComprador).get(idDir)

    print(direccion_usuario)
    if ( direccion_usuario is None):
        return jsonify({"mensaje:": "No se pudo eliminar. El " + _tipo_usuario + " con correo <" + correo + "> no tiene una direccion con id <" + str(idDir) + ">."})

    db.session.delete(direccion_usuario)
    db.session.commit()

    return jsonify({"mensaje:": "Se elimino correctamente la direccion <" + str(idDir) + "> del " + _tipo_usuario + " con correo <" + correo + ">."})
'''