from flask import Blueprint, request, jsonify
from models.opinarM import Opinar
from schemas.opinarS import OpinarEsquema
from schemas.opinionCompleta import OpinarCompletaEsquema
from main import db
from sqlalchemy import *

resena = Blueprint('resena', __name__)
engine = create_engine('mysql+pymysql://root:pruebatest@localhost/mydb')
opinion_esquema = OpinarEsquema()
opiniones_esquema = OpinarEsquema(many=True)

opinionCompleta_esquema = OpinarCompletaEsquema()

opinionCompletas_esquema = OpinarCompletaEsquema(many = True)


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
@resena.route('/resenas/<id>', methods=['GET'])
def ver_5_resenas(id):
     #diccionario en python
     resenas = engine.execute('select * from comprador  inner join opinar where comprador.correo = opinar.correo')
     
     
     print(resenas)
               #Creamos un archivo json con el diccionario que le pedimos a nuestra BD

     return opinionCompletas_esquema.jsonify(resenas)

