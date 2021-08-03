from flask_mail import Mail, Message
from flask import current_app as app
from main import db
from flask import Blueprint, request
from models.compraM import Compra
from models.compradorM import Comprador
from schemas.compraS import CompraEsquema
from pprint import pprint

compra = Blueprint('compra', __name__)

compra_esquema = CompraEsquema()
compras_esquema = CompraEsquema(many=True)

@compra.route('/compra', methods=['POST'])
def finalizar_compra():
    correo = request.json['correo']    
    # Ingreso la tarjeta ya cifrada
    idDir = request.json['idDir']
    tarjeta = request.json['tarjeta']
    total = request.json['total']    
    compra_nueva = Compra(correo, idDir, tarjeta, total)

    nombre = Comprador.query.get(correo).nombre
    pprint(nombre)
    enviar_correo(correo, nombre, total)
    db.session.add(compra_nueva)
    db.session.commit()

    return compra_esquema.jsonify(compra_nueva)

def enviar_correo(correo, nombre, total):
    mail = Mail(app)
    try:
        mensaje = Message('Compra en DeVolada', sender='mercadodevolada@gmail.com', recipients=[f'{correo}'])
        mensaje.body = f"Hola  {nombre}! \n Gracias por realizar tu compra en DeVolada\n El total de tu compra es de {total} pesos"
        mail.send(mensaje)
    except Exception as e:
        print("Excepción: \n")
        print(e)
        raise    
    return "Correo enviado :)"
