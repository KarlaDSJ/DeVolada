from flask import Blueprint, request, jsonify
from models.opinarM import Opinar
from schemas.opinarS import OpinarEsquema
from main import db

resena = Blueprint('resena', __name__)

opinion_esquema = OpinarEsquema()
opiniones_esquema = OpinarEsquema(many=True)

@resena.route('/mostrarResenas', methods=['GET','POST'])
def ver_resenas():
     idProducto = request.json['idProducto']

     #diccionario en python
     resenas = Opinar.query.filter_by(idProducto=idProducto).all()

     #Creamos un archivo json con el diccionario que le pedimos a nuestra BD
     return opiniones_esquema.jsonify(resenas)

@resena.route('/crearResena', methods=['POST'])
def crear_resena():
     correo = request.json['correo']
     idProducto = request.json['idProducto']
     opinion = request.json['opinion']
     calificacion = request.json['calificacion']

     resena_nueva = Opinar(correo, idProducto, opinion, calificacion)

     db.session.add(resena_nueva)
     db.session.commit()

     return jsonify({'mensaje':'todo bien'})

#Funcion que muestra las primeras 5 reseñas de un producto
@resena.route('/resenas', methods=['GET'])
def ver_5_resenas():
     idProducto = request.json['idProducto']

     #diccionario en python
     resenas = Opinar.query.filter_by(username=idProducto).limit(5)

     #Creamos un archivo json con el diccionario que le pedimos a nuestra BD
     return jsonify(resenas)