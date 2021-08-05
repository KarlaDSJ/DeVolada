from main import db
from flask import Blueprint, request, jsonify
from models.direccionVendedorM import DireccionVendedor
from schemas.direccionE import DireccionEsquema


direccionVendedor = Blueprint('direccionVendedor', __name__)

direccionVendedor_esquema = DireccionEsquema()


# Petición para agregar una direccion de vendedor a la base de datos.
@direccionVendedor.route('/direccion/vendedor', methods=['POST'])
def agrega_direccion():
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


# Petición para obtener la direccion del vendedor en la base de datos.
@direccionVendedor.route('/direccion/vendedor', methods=['GET'] )
def obten_direccion():
    correo  = request.json['correo']
    direccion = db.session.query(DireccionVendedor).filter_by(correo=correo).first()
    return direccionVendedor_esquema.jsonify(direccion)


# Petición para actualizar la direccion del vendedor en la base de datos.
@direccionVendedor.route('/direccion/vendedor', methods=['PATCH'])
def actualiza_direccion():
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

