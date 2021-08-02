from main import db
from flask import Blueprint, request, jsonify
from models.pertenecerM import Pertenecer
from schemas.pertenecerE import PertenecerEsquema

pertenecer = Blueprint('pertenecer',__name__)

pertenecer_esquema = PertenecerEsquema()
pertenecers_esquema = PertenecerEsquema(many=True)

@pertenecer.route('/pertenecer/correo', methods=['GET'])
def obtener_datos():    
    correo = request.args.get('correo', '')    
    pertenecer = Pertenecer.query.filter_by(correo=correo).first()
    
    if pertenecer is None:
        return jsonify({'msg': 'No existe un carrito para ese comprador :('})
    else:
        return jsonify({'id_carrito': pertenecer.idCarrito})


@pertenecer.route('/pertenecer/carrito', methods=['GET'])
def obtener_dueno():    
    idCarrito = request.args.get('idCarrito', '')
    pertenecer = Pertenecer.query.filter_by(idCarrito=idCarrito).first()
    
    if pertenecer is None:
        return jsonify({'msg': 'No existe un comprador asignado a ese carrito :('})
    else:
        return jsonify({'dueno': pertenecer.correo})


@pertenecer.route('/pertenecer', methods=['POST'])
def relacion_carrito_comprador():  
    correo = request.json['correo']
    idCarrito = request.json['idCarrito']
    pertenecer_nuevo = Pertenecer(correo, idCarrito)

    db.session.add(pertenecer_nuevo)
    db.session.commit()        
    return pertenecer_esquema.jsonify(pertenecer_nuevo)