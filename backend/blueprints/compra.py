from flask_mail import Mail, Message
from flask import current_app as app
from main import db
from flask import Blueprint, request
from models.compraM import Compra
from schemas.compraS import compraEsquema
# from schemas.productoE import ProductoEsquema

compra = Blueprint('compra', __name__)

compra_esquema = compraEsquema()
compras_esquema = compraEsquema(many=True)

@compra.route('/compra', methods=['POST'])
def finalizar_compra():
    correo = request.json['correo']    
    nombre = request.json['nombre']
    tarjeta = request.json['tarjeta']
    idDir = request.json['idDir']
    total = request.json['total']

    enviar_correo(correo, nombre, total)

    compra_nueva = Compra(correo, idDir, tarjeta)


    db.session.add(compra_nueva)
    db.session.commit()

def enviar_correo(correo, nombre, total):
    mail = Mail(app)
    try:
        mensaje = Message("DeVolada", sender="mercadodevolada@gmail.com", recipients = [correo])
        
        mensaje.body = f"Hola  {nombre}! \n Gracias por realizar tu compra en DeVolada \n El total de tu compra es {total}"
        mail.send(mensaje)
    except Exception:
        raise
    return "Correo enviado :)"
