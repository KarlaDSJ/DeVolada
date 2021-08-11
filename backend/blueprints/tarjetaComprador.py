from main import db
from flask import Blueprint, request, jsonify
from models.tarjetaCompradorM import TarjetaComprador, generar_codigo
from schemas.tarjetaCompradorE import TarjetaCompradorEsquema

from marshmallow import Schema, fields
from pprint import pprint

tarjetaComprador = Blueprint('tarjetaComprador', __name__)

tarjetaComprador_esquema = TarjetaCompradorEsquema()
tarjetaCompradores_esquema = TarjetaCompradorEsquema( many=True)


@tarjetaComprador.route('/tarjetaComprador', methods=['POST'])
def agregar_tarjeta():

    correo = request.json['correo']
    numero = request.json['numero']
    cvv = request.json['cvv']
    duenio = request.json['duenio']
    fechaCad = request.json['fechaCad']

    tarjetaComprador_nuevo = TarjetaComprador(correo, numero, duenio, fechaCad, cvv)
    db.session.add(tarjetaComprador_nuevo)
    db.session.commit()

    num = obtener_codigo(tarjetaComprador_nuevo.numero)
    return jsonify({'numero': num, 'dueno': tarjetaComprador_nuevo.dueno})    


@tarjetaComprador.route('/tarjetaComprador', methods=['GET'])
def obtener_tarjeta():
    '''
    Obtiene el número de una tarjeta en específico
    de un comprador. Se necesitan del correo y el
    número de tarjeta en la ruta como parámetros

    Returns: json con el número de tarjeta cifrado 
    del comprador 
    '''

    correo = request.args.get('correo', '')
    numero = request.args.get('numero', '')
    num_cifrado = generar_codigo(numero)
    tarjeta = TarjetaComprador.query.get((num_cifrado,correo))       
    return jsonify({'tarjeta':tarjeta.numero})   


@tarjetaComprador.route('/tarjetasComprador', methods=['GET'])
def obtener_tarjetas():
    '''
    Obtiene todas las tarjetas de un comprador,
    se necesita del correo como parámetro de la ruta

    Returns: Lista con todos los números de tarjetas
    registradas de un comprador
    '''

    correo = request.args.get('correo', '')    
    tarjetas = TarjetaComprador.query.filter_by(correo=correo).all()
    datos = tarjetaCompradores_esquema.dump(tarjetas) 

    for item in datos:
        x = item['numero']
        item.update({'tarjeta': obtener_codigo(x)})
        item.pop('numero')

    return jsonify(datos)  


def obtener_codigo(item):
    """
    Obtiene el número de tarjeta original dada 
    la cifrada

    Params:
        item: número de tarjeta cifrada 
    Returns: Número de tarjeta original 
    """
    viejo = ""
    for i in range(0,len(item),1):
        viejo+=str(  (int(item[i])-3)  %  10)
    return viejo