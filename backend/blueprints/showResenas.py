from flask import Blueprint, request, jsonify
from models.opinarM import Opinar
from main import db

showResenas = Blueprint('showResenas', __name__)

#Funcion que muestra todas las reseñas de un producto
@showResenas.route('/mostrarResenas', methods=['GET','POST'])
def ver_resenas():
     idProducto = request.json['idProducto']

     #diccionario en python
     resenas = Opinar.query.filter_by(username=idProducto).all()

     #Creamos un archivo json con el diccionario que le pedimos a nuestra BD
     return jsonify(resenas)

#Funcion que muestra las primeras 5 reseñas de un producto
@showResenas.route('/resenas', methods=['GET'])
def ver_5_resenas():
     idProducto = request.json['idProducto']

     #diccionario en python
     resenas = Opinar.query.filter_by(username=idProducto).limit(5)

     #Creamos un archivo json con el diccionario que le pedimos a nuestra BD
     return jsonify(resenas)