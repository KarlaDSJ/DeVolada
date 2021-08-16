from flask_mail import Mail, Message
from flask import current_app as app
from main import db
from flask import Blueprint, request, jsonify
from models.compraM import Compra
from models.compradorM import Comprador
from models.productoM import Producto
from models.incluirM import Incluir
from schemas.compraS import CompraEsquema
from schemas.incluirE import IncluirEsquema
from schemas.productoS import ProductoEsquema
from pprint import pprint

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones sobre una compra
"""

compra = Blueprint('compra', __name__)

"""---------------- Esquemas ----------------"""

compra_esquema = CompraEsquema()
compras_esquema = CompraEsquema(many=True)

"""---------------- Rutas ----------------"""

@compra.route('/compra', methods=['POST'])
def finalizar_compra():
    """
    Finaliza una compra

    Returns:
    Json con la info de la compra.
    No incluye los productos comprados.
    """

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


@compra.route('/compra/<id_compra>', methods=['GET'])
def productos_comprados (id_compra):
    '''
    Obtiene todos los productos comprados en una compra 
    en una lista de json
    
    Params:
        id_compra: identificador de la compra de la que se quiere 
                   saber la info
    Returns:
    Lista de los productos y sus cantidades en formato json
    '''

    compra = Compra.query.get(id_compra)  
    productos_incluidos = Incluir.query.filter_by(idCompra=id_compra).all()
    inclusion_esquema = IncluirEsquema(many=True, only=('idProducto', 'cantidad'))
    datos = inclusion_esquema.dump(productos_incluidos)

    producto_esquema = ProductoEsquema(
        only=("idProducto", "nombre", "imagenes"))

    for item in datos:        
        x = item.pop('idProducto')
        prod = Producto.query.get(x)
        # Disminuyo la cantidad de cada producto en los disponibles
        prod.disponibles -= item['cantidad']
        db.session.commit()
        # Agregó la información al json 
        informacion = producto_esquema.dump(prod)
        item.update(informacion)

    return jsonify(datos)


def enviar_correo(correo, nombre, total):
    '''
    Manda un correo con el total de la compra a un comprador
    
    Params:
        correo: destinatario
        nombre: nombre del comprador
        total: total de la compra    
    Returns: 
    Mensaje indicando que se ha enviado
    '''

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
