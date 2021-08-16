from flask import Blueprint, request, jsonify #Para poder hacer los JSON
from models.opinarM import Opinar #El modelo de Opinar
from schemas.opinarS import OpinarEsquema #Esquema de Opinar
from schemas.opinionCompleta import OpinarCompletaEsquema #Esquema de Opinion Completa
from schemas.promedioE import Promedio #Esquema de Promedio
from main import db # Importamos la instanica de la base de datos
from sqlalchemy import * # Importamos sqlalchemy 
import simplejson #Importamos simplejson
import json #Importamos json

# Inicializamos el blueprint
resena = Blueprint('resena', __name__)
engine = create_engine('mysql+pymysql://root:pruebatest@localhost/mydb')
opinion_esquema = OpinarEsquema()
opiniones_esquema = OpinarEsquema(many=True)

opinionCompleta_esquema = OpinarCompletaEsquema()
opinionCompletas_esquema = OpinarCompletaEsquema(many = True)

promedio_Esquema = Promedio(many=True)

"""
Método que muestra todas las reseñas de un producto

return un archivo JSON con los datos de todas las reseñas del producto
"""

@resena.route('/mostrarResenas/<id>', methods=['GET','POST'])
def ver_resenas(id):
     text = 'select * from comprador  inner join opinar where comprador.correo = opinar.correo and idProducto = ' + id + ' '
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)
     
     print(resenas)

     return opinionCompletas_esquema.jsonify(resenas)


"""
Método que crear un reseña (calificacion y comentario de un usuario)

return un archivo JSON con los datos de la nueva reseña creada
manda un mensaje de: todo bien
"""

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


"""
Método que muestra en la página de producto (en la parte de abajo), 
las primeras 5 reseñas hechas por otros usuarios

return un archivo JSON con los datos de los 5 primeros comentarios
"""

@resena.route('/resenas/<id>', methods=['GET'])
def ver_5_resenas(id):
     text = 'select * from comprador  inner join opinar where comprador.correo = opinar.correo and idProducto = ' + id + ' order by idProducto desc limit 5'
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)

     print(resenas)
          
     return opinionCompletas_esquema.jsonify(resenas)


"""
Método que regresa el promedio de todas las calificaciones que se han dejado en un producto

return una cadena de datos JSON con el promedio de todas las de calificaciones
"""

@resena.route('/promedio/<id>', methods=['GET'])
def promedio(id):
     text = 'select avg(calificacion) from opinar where opinar.idProducto= ' + id +' group by idProducto'
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)

     for i in resenas:
          promedio=(i['avg(calificacion)'])
          
     promedio = "{0:.1f}".format(promedio)

     return simplejson.dumps({'promedio':promedio})


"""
Método que regresa el # total de calificaciones que se han dejado en un producto

return una cadena de datos JSON con el # total de calificaciones
"""

@resena.route('/totalResenas/<id>', methods=['GET'])
def resenasTotal(id):
     text = 'select count(calificacion) from opinar where opinar.idProducto= ' + id +' group by idProducto'
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)

     for i in resenas:
          total=(i['count(calificacion)'])
     
     return simplejson.dumps({'total':total})