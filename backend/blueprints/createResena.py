from flask import Blueprint, request, jsonify
from models.opinarM import Opinar
from main import db

createResena = Blueprint('createResena', __name__)

@createResena.route('/crearResena', methods=['POST'])
def crear_resena():
     correo = request.json['correo']
     idProducto = request.json['idProducto']
     opinion = request.json['opinion']
     calificacion = request.json['calificacion']

     resena_nueva = Opinar(correo, idProducto, opinion, calificacion)

     db.session.add(resena_nueva)
     db.session.commit()

     return resena_nueva.jsonify({'mensaje':'todo bien'})
