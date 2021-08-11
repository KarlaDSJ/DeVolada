from main import db
from flask import Blueprint, request, jsonify
from models.pertenecerM import Pertenecer
from schemas.pertenecerE import PertenecerEsquema

pertenecer = Blueprint('pertenecer',__name__)

pertenecer_esquema = PertenecerEsquema()
pertenecers_esquema = PertenecerEsquema(many=True)

@pertenecer.route('/pertenecer/correo', methods=['GET'])
def obtener_datos():    
    '''
    Obtiene el carrito de un comprador dado su correo

    Returns: Json indicando el identificador del carrito
    o error 404 indicando que no existe un carrito para 
    ese comprador
    '''
    correo = request.args.get('correo', '')    
    pertenecer = Pertenecer.query.filter_by(correo=correo).first()
    
    if pertenecer is None:
        return jsonify({'msg': 'No existe un carrito para ese comprador :('}), 404
    else:
        return jsonify({'msg': pertenecer.idCarrito})

@pertenecer.route('/pertenecer', methods=['POST'])
def relacion_carrito_comprador():  
    '''
    Crea una relación entre un carrito y un comprador 
    Requiere del correo y el idCarrito por el 'body'
    en formato json

    Returns: Información de la relación en un json
    '''
    correo = request.json['correo']
    idCarrito = request.json['idCarrito']
    pertenecer_nuevo = Pertenecer(correo, idCarrito)

    db.session.add(pertenecer_nuevo)
    db.session.commit()        
    return pertenecer_esquema.jsonify(pertenecer_nuevo)