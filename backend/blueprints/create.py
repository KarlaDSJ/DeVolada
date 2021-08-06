from flask import Blueprint 
from flask import request
from models.compradorM import Comprador
from models.vendedorM  import Vendedor 
from main import db    
from flask.json import jsonify
from schemas.compradorE import CompradorEsquema
from schemas.vendedorE import VendedorEsquema
from models.direccionCompradorM import DireccionComprador
from models.direccionVendedorM import DireccionVendedor
from models.tarjetaVendedorM import TarjetaVendedor
from schemas.direccionE import DireccionEsquema
from random import choice
from flask import current_app as app
from flask_mail import Message,Mail
import re

create = Blueprint('create',__name__)

comprador_esquema = CompradorEsquema()
compradores_esquema = CompradorEsquema(many=True)

vendedor_esquema = VendedorEsquema()
vendedores_esquema = VendedorEsquema(many=True)

direccion_esquema = DireccionEsquema()
direccion_esquema = DireccionEsquema(many=True)



@create.route('/createC', methods=['POST'])
def agrega_comprador():
    correo = request.json['correoC']
   
    nombre = request.json['nombreC']
    telefono = request.json['telefonoC']
    estado = request.json['estadoC']
    ciudad = request.json['ciudadC']
    colonia = request.json['coloniaC']
    cp = request.json['cpC']
    calle = request.json['calleC']
    numero = request.json['numeroC']
    contraseniaRandom = "Admin"
    
    
    longitud = 8
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    contraseniaRandom = ""
    contraseniaRandom = contraseniaRandom.join([choice(valores) for i in range(longitud)])
    comprador = Comprador.query.filter_by(correo = correo).first()
    
    if(comprador is None):
        if(verificar_arroba(correo)):
            enviar_correo(correo, nombre, contraseniaRandom)
            direccion_nueva = DireccionComprador(correo, estado, ciudad, colonia, cp, calle, numero)
            comprador_nuevo = Comprador(correo, nombre, telefono, contraseniaRandom)
            db.session.add(comprador_nuevo)
            db.session.commit()
            db.session.add(direccion_nueva)
            db.session.commit()
            return jsonify({'msg':'success'})
        else:
            return jsonify({'msg':'error_correo'})
    else: 
        return jsonify({'msg':'correo_registrado'})

@create.route('/createV', methods=['POST'])
def agrega_vendedor():

    correo = request.json['correoV']
    nombre = request.json['nombreV']
    telefono = request.json['telefonoV']
    estado = request.json['estadoV']
    ciudad = request.json['ciudadV']
    colonia = request.json['coloniaV']
    cp = request.json['cpV']
    calle = request.json['calleV']
    numero = request.json['numeroV']

    tarjeta = request.json['tarjetaV']
    

  
    longitud = 8
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    contraseniaRandom = ""
    contraseniaRandom = contraseniaRandom.join([choice(valores) for i in range(longitud)])
    vendedor = Vendedor.query.filter_by(correo = correo).first()
    if(vendedor is None):
        if(verificar_arroba(correo)):
            enviar_correo(correo, nombre, contraseniaRandom)
            direccion_nueva = DireccionVendedor(correo, estado, ciudad, colonia, cp, calle, numero)
            vendedor_nuevo = Vendedor(correo, nombre, telefono, contraseniaRandom)
            tarjeta_nueva = TarjetaVendedor(correo, tarjeta) 
            db.session.add(vendedor_nuevo)
            db.session.commit()
            db.session.add(direccion_nueva)
            db.session.commit()
            db.session.add(tarjeta_nueva)
            db.session.commit()
            return jsonify({'msg':'success'})
        else:
            return jsonify({'msg':'error_correo'})
    else: 
        return jsonify({'msg':'correo_registrado'})
        
    
def enviar_correo(correo, nombre, contrasenia):
    mail = Mail(app)
    try:

        mensaje = Message('DeVolada',sender= 'marcoordunaavila@gmail.com', recipients = [correo])
        mensaje.body = f"Confirmación de corrreo \n  Hola {nombre} \n Esta es tu contraseña con la que puedes acceder al sistema: {contrasenia} \n"
        
        mail.send(mensaje)
    except Exception:
        raise
    return "Correo enviado :)"

def verificar_arroba(correo):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
	    return True
    else:
	    return False   

