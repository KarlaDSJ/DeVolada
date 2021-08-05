from main import db
from flask import Blueprint, request, jsonify
from models.vendedorM import Vendedor
from schemas.vendedorE import VendedorEsquema
from pprint import pprint
vendedor = Blueprint('vendedor',__name__)

vendedor_esquema = VendedorEsquema()
vendedores_esquema = VendedorEsquema(many=True)

@vendedor.route('/vendedor/<correo>', methods=['GET'])
def obtener_vendedor(correo):    
    vendedor = Vendedor.query.get(correo)
    pprint(vendedor)
    return jsonify({'correo': vendedor.correo, 'nombre': vendedor.nombre,
                    'telefono': vendedor.telefono})


@vendedor.route('/vendedor', methods=['POST'])
def agrega_vendedor():
    correo = request.json['correo']
    nombre = request.json['nombre']
    telefono = request.json['telefono']
    contrasenia = request.json['contrasenia']

    vendedor_nuevo = Vendedor(correo, nombre, telefono, contrasenia)

    db.session.add(vendedor_nuevo)
    db.session.commit()

    return vendedor_esquema.jsonify(vendedor_nuevo)