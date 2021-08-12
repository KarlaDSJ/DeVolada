from main import db # importamos la instanica de la base de datos
from flask import Blueprint, request, jsonify # para poder hacer los JSON
from models.compradorM import Comprador # el modelo del Comprador
from schemas.compradorE import CompradorEsquema # el schema del Comprador

""" 
Archivo de rutas para poder manejar las peticiones sobre el comprador
"""

# Inicializamos el blueprint

comprador = Blueprint('comprador',__name__)

# Instnaciamos los eschemas

comprador_esquema = CompradorEsquema()
compradores_esquema = CompradorEsquema(many=True)

""" 
Metodo para obtener los datos del comprador segun su id

return un JSON con los datos del comprador
"""

@comprador.route('/comprador/<correo>', methods=['GET'])
def obtener_comprador(correo):    
    comprador = Comprador.query.get(correo)
    return comprador_esquema.jsonify(comprador)

"""
Metodo para agregar un nuevo comprador

return un JSON con los datos del nuevo comprador 
"""

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