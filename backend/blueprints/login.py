from models.vendedorM import Vendedor # el modelo del vendedor
from flask import Blueprint # El blueprint
from flask import session # manejamos las sesiones desde el servidor para que se le sea imposible a una persona acceder desde fuera
from flask.json import jsonify # para hacer el JSON de las peticiones
from models.compradorM import Comprador #El modelo del comprador
from flask import request # para pedir las peticiones por http

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

""" 
Archivo de rutas para poder manejar las peticiones para iniciar sesión
"""

# Instancia al blueprint

login = Blueprint('login',__name__)


@login.route('/loginC', methods = ['GET', 'POST'])
def entrarC():
    """
    Metodo para darle acceso al comprador

    Params:        
        correoC: identificador del comprador
        contraseniaC: contraseña del comprador
    Returns: un menaje de si el usuario se registro correctamente, 
    si no, entonces manda un mensaje con el error
    """

    correo = request.json['correoC']
    contrasenia = request.json['contraseniaC']
    comprador = Comprador.query.filter_by(correo = correo).first() #consulta de SQL
    if (comprador is not None ):
        if (comprador.correo == correo and comprador.verify_password(contrasenia) ):
            session['email'] = correo
            sesionActiva = session['email']
            return jsonify({'msg':'success','session':sesionActiva, 'nombre': comprador.nombre })
        else:
            return jsonify({'msg': 'error_contrasenia'})
    else:
        return jsonify({'msg': 'error_datos'}) 


@login.route('/loginV', methods = ['GET', 'POST'])
def entrarV():
    """
    Método para darle acceso al vendedor

    Params:        
        correoC: identificador del comprador
        contraseniaC: contraseña del comprador
    Returns: n mensaje de si el usario se registró correctamente, 
    si no, manda un mensaje de error
    """

    correo = request.json['correoV']
    contrasenia = request.json['contraseniaV']
    vendedor = Vendedor.query.filter_by(correo = correo).first() #consulta SQL
    if (vendedor is not None ):
        if (vendedor.correo == correo and vendedor.verify_password(contrasenia) ):
            session['email'] = correo
            sesionActiva = session['email']
            return jsonify({'msg':'success','session':sesionActiva, 'nombre': vendedor.nombre })
        else: 
            return jsonify({'msg': 'error_contrasenia'})
    else:
        return jsonify({'msg': 'error_datos'})

