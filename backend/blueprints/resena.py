from flask import Blueprint, request, jsonify
from models.opinarM import Opinar
from schemas.opinarS import OpinarEsquema
from schemas.opinionCompleta import OpinarCompletaEsquema
from schemas.promedioE import Promedio
from main import db
from sqlalchemy import *
import simplejson
import json

resena = Blueprint('resena', __name__)
engine = create_engine('mysql+pymysql://root:pruebatest@localhost/mydb')
opinion_esquema = OpinarEsquema()
opiniones_esquema = OpinarEsquema(many=True)

opinionCompleta_esquema = OpinarCompletaEsquema()

opinionCompletas_esquema = OpinarCompletaEsquema(many = True)

promedio_Esquema = Promedio(many=True)

#Funcion que muestra todas las reseñas de un producto
@resena.route('/mostrarResenas/<id>', methods=['GET','POST'])
def ver_resenas(id):
     text = 'select * from comprador  inner join opinar where comprador.correo = opinar.correo and idProducto = ' + id + ' '
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)
     
     
     print(resenas)
               #Creamos un archivo json con el diccionario que le pedimos a nuestra BD

     return opinionCompletas_esquema.jsonify(resenas)

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
     text = 'select * from comprador  inner join opinar where comprador.correo = opinar.correo and idProducto = ' + id + ' order by idProducto desc limit 5'
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)
     
     
     print(resenas)
               #Creamos un archivo json con el diccionario que le pedimos a nuestra BD

     return opinionCompletas_esquema.jsonify(resenas)


@resena.route('/promedio/<id>', methods=['GET'])
def promedio(id):
     text = 'select avg(calificacion) from opinar where opinar.idProducto= ' + id +' group by idProducto'
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)

     for i in resenas:
          promedio=(i['avg(calificacion)'])
          
     promedio = "{0:.1f}".format(promedio)
     
               #Creamos un archivo json con el diccionario que le pedimos a nuestra BD
     return simplejson.dumps({'promedio':promedio})


@resena.route('/totalResenas/<id>', methods=['GET'])
def resenasTotal(id):
     text = 'select count(calificacion) from opinar where opinar.idProducto= ' + id +' group by idProducto'
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)

     for i in resenas:
          total=(i['count(calificacion)'])
     
               #Creamos un archivo json con el diccionario que le pedimos a nuestra BD
     return simplejson.dumps({'total':total})