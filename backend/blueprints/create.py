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
from flask import render_template
import re

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones para crear un usuario
"""

create = Blueprint('create',__name__)

"""---------------- Esquemas ----------------"""

comprador_esquema = CompradorEsquema()
compradores_esquema = CompradorEsquema(many=True)

vendedor_esquema = VendedorEsquema()
vendedores_esquema = VendedorEsquema(many=True)

direccion_esquema = DireccionEsquema()
direccion_esquema = DireccionEsquema(many=True)

"""---------------- Rutas ----------------"""

@create.route('/createC', methods=['POST'])
def agrega_comprador():
    """
    Registra a un comprador en la base de datos
    Params:        
        correoC: correo del comprador
        nombreC: nombre del comprador
        telefonoC: teléfono del comprador
        estadoC: estado en donde vive
        ciudadC: ciudad en donde vive
        coloniaC: colonia en donde vive
        cpC: código postal 
        calleC: calle en donde vive
        numeroC: número de la casa
    Returns: mensaje de éxito o error al registrar
    """

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
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+"
    contraseniaRandom = ""
    contraseniaRandom = contraseniaRandom.join([choice(valores) for i in range(longitud)])
    comprador = Comprador.query.filter_by(correo = correo).first()
    
    if(comprador is None):
        if(verificar_arroba(correo)):
            enviar_correoC(correo, nombre, contraseniaRandom)
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
    """
    Registra a un vendedor en la base de datos
    Params:        
        correoV: correo del vendedor
        nombreV: nombre del vendedor
        telefonoV: teléfono del cvendedor
        estadoV: estado en donde vive
        ciudadV: ciudad en donde vive
        coloniaV: colonia en donde vive
        cpV: código postal 
        calleV: calle en donde vive
        numeroV: número de la casa
    Returns: mensaje de éxito o error al registrar
    """
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
            enviar_correoV(correo, nombre, contraseniaRandom)
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
        
    
def enviar_correoC(correo, nombre, contrasenia):
    """
    Envia un correo con los datos al comprador
    Params:        
        correo: correo del comprador
        nombre: nombre del comprador
        contrasenia: contraseña generada por el sistema 
                     para el comprador
    Returns: mensaje de éxito o error al enviar el correo
    """

    mail = Mail(app)
    try:

        mensaje = Message('DeVolada',sender= 'marcoordunaavila@gmail.com', recipients = [correo])
        mensaje.body = "holiwis"

        
        mensaje.html = f'''<!doctype html> <html lang="en">   <head>    <!-- Required meta tags -->    <meta charset="utf-8">    <meta name="viewport" content="width=device-width, initial-scale=1">    <!-- Bootstrap CSS -->    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">   <title>Hello, world!</title>  </head>  <body>    
        <div class="card text-center">
        <h1>DeVolada.com</h1>
        <a href="https://imgbb.com/"><img src="https://i.ibb.co/BtGkC8p/DV.png" alt="DV" border="0"></a>
        <div class="card-header" style="margin-top: 10px;">
          Gracias por registrarte  {nombre} como comprador
        </div>
        <div class="card-body">
          <h5 class="card-title">Esta es la contraseña con la que podras acceder al sistema: </h5> 
          <h3>{contrasenia} </h3>
          <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
          <a href="#" class="btn btn-primary">DeVolada</a>
        </div>
        <div class="card-footer text-muted">
          
        </div>
         </div>
    
    
         <!-- Option 1: Bootstrap Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>

         <!-- Option 2: Separate Popper and Bootstrap JS -->
         <!--
         <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
            -->
         </body>
         </html>'''
    
        mail.send(mensaje)
    except Exception:
        raise
    return "Correo enviado :)"


def enviar_correoV(correo, nombre, contrasenia):
    """
    Envia un correo con los datos al vendedor
    Params:        
        correo: correo del vendedor
        nombre: nombre del vendedor
        contrasenia: contraseña generada por el sistema 
                     para el vendedor
    Returns: mensaje de éxito o error al enviar el correo
    """

    mail = Mail(app)
    try:

        mensaje = Message('DeVolada',sender= 'marcoordunaavila@gmail.com', recipients = [correo])
        mensaje.body = "holiwis"

        
        mensaje.html = f'''<!doctype html> <html lang="en">   <head>    <!-- Required meta tags -->    <meta charset="utf-8">    <meta name="viewport" content="width=device-width, initial-scale=1">    <!-- Bootstrap CSS -->    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">   <title>Hello, world!</title>  </head>  <body>    
        <div class="card text-center">
        <h1>DeVolada.com</h1>
        <a href="https://imgbb.com/"><img src="https://i.ibb.co/BtGkC8p/DV.png" alt="DV" border="0"></a>
        <div class="card-header" style="margin-top: 10px;">
          Gracias por registrarte  {nombre} como vendedor
        </div>
        <div class="card-body">
          <h5 class="card-title">Esta es la contraseña con la que podras acceder al sistema: </h5> 
          <h3>{contrasenia} </h3>
          <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
          <a href="#" class="btn btn-primary">DeVolada</a>
        </div>
        <div class="card-footer text-muted">
          
        </div>
         </div>
    
    
         <!-- Option 1: Bootstrap Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>

         <!-- Option 2: Separate Popper and Bootstrap JS -->
         <!--
         <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
            -->
         </body>
         </html>'''
    
        mail.send(mensaje)
    except Exception:
        raise
    return "Correo enviado :)"

def verificar_arroba(correo):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
	    return True
    else:
	    return False   

