from flask import Blueprint, request, jsonify
from models.opinarM import Opinar
from schemas.opinarS import OpinarEsquema
from schemas.opinionCompleta import OpinarCompletaEsquema
from schemas.promedioE import Promedio
from main import db
from sqlalchemy import *
import simplejson
import json


__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones para crear una reseña
"""

resena = Blueprint('resena', __name__)
engine = create_engine('mysql+pymysql://root:pruebatest@localhost/mydb')

"""---------------- Esquemas ----------------"""

opinion_esquema = OpinarEsquema()
opiniones_esquema = OpinarEsquema(many=True)

opinionCompleta_esquema = OpinarCompletaEsquema()
opinionCompletas_esquema = OpinarCompletaEsquema(many = True)

promedio_Esquema = Promedio(many=True)
"""---------------- Rutas ----------------"""

#Funcion que muestra todas las reseñas de un producto
@resena.route('/mostrarResenas/<id>', methods=['GET','POST'])
def ver_resenas(id):
     """
     Muestra todas las reseñas de un producto
     Params:        
          id: identificador del producto
     Returns: lista de las reseñas
     """

     text = 'select * from comprador  inner join opinar where comprador.correo = opinar.correo and idProducto = ' + id + ' '
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)
     
     
     print(resenas)
               #Creamos un archivo json con el diccionario que le pedimos a nuestra BD

     return opinionCompletas_esquema.jsonify(resenas)

@resena.route('/crearResena', methods=['POST'])
def crear_resena():
     """
     Crea una reseña para un producto
     Returns: mensaje de éxito
     """

     correo = request.json['correo']
     idProducto = request.json['idProducto']
     opinion = request.json['opinion']
     calificacion = request.json['calificacion']

     resena_nueva = Opinar(correo, idProducto, opinion, calificacion)

     db.session.add(resena_nueva)
     db.session.commit()

     return jsonify({'mensaje':'todo bien'})


@resena.route('/resenas/<id>', methods=['GET'])
def ver_5_resenas(id):
     """
     Muestra las primeras 5 reseñas de un producto
     Params:        
          id: identificador del producto
     Returns: lista de las reseñas
     """

     text = 'select * from comprador  inner join opinar where comprador.correo = opinar.correo and idProducto = ' + id + ' order by idProducto desc limit 5'
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)
     
     
     print(resenas)
               #Creamos un archivo json con el diccionario que le pedimos a nuestra BD

     return opinionCompletas_esquema.jsonify(resenas)


@resena.route('/promedio/<id>', methods=['GET'])
def promedio(id):
     """
     Calcula la calificación de un producto según las reseñas
     Params:        
          id: identificador del producto
     Returns: calificación del producto
     """

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
     """
     Cuenta el número de reseñas de un producto
     Params:        
          id: identificador del producto
     Returns: número de reseñas de un producto
     """

     text = 'select count(calificacion) from opinar where opinar.idProducto= ' + id +' group by idProducto'
     print(text) 
     #diccionario en python
     resenas = engine.execute(text)

     for i in resenas:
          total=(i['count(calificacion)'])
     
               #Creamos un archivo json con el diccionario que le pedimos a nuestra BD
     return simplejson.dumps({'total':total})