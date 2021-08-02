from main import db
from flask import Blueprint, request, jsonify
from models.compradorM import Comprador
from schemas.compradorE import CompradorEsquema

comprador = Blueprint('comprador',__name__)

comprador_esquema = CompradorEsquema()
compradores_esquema = CompradorEsquema(many=True)

@comprador.route('/comprador/<correo>', methods=['GET'])
def obtener_comprador(correo):    
    comprador = Comprador.query.get(correo)
    # return jsonify({'correo': comprador.correo, 'nombre': comprador.nombre,
    #                 'telefono': comprador.telefono})
    return comprador_esquema.jsonify(comprador)


@comprador.route('/comprador', methods=['POST'])
def agrega_comprador():
    correo = request.json['correo']
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    contrasenia = request.json['contrasenia']

    comprador_nuevo = Comprador(correo, nombre, telefono, contrasenia)

    db.session.add(comprador_nuevo)
    db.session.commit()

    return comprador_esquema.jsonify(comprador_nuevo)