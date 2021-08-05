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

    correo = request.args.get('correo', '')
    numero = request.args.get('numero', '')
    num_cifrado = generar_codigo(numero)
    tarjeta = TarjetaComprador.query.get((num_cifrado,correo))    
    num = obtener_codigo(tarjeta.numero)
    pprint(num)
    return jsonify({'tarjeta':tarjeta.numero})   


@tarjetaComprador.route('/tarjetasComprador', methods=['GET'])
def obtener_tarjetas():

    correo = request.args.get('correo', '')    
    tarjetas = TarjetaComprador.query.filter_by(correo=correo).all()
    datos = tarjetaCompradores_esquema.dump(tarjetas) 

    for item in datos:
        pprint(item)
        x = item['numero']
        item.update({'tarjeta': obtener_codigo(x)})
        item.pop('numero')

    return jsonify(datos)  


def obtener_codigo(item):
    viejo = ""
    for i in range(0,len(item),1):
        viejo+=str(  (int(item[i])-3)  %  10)
    return viejo