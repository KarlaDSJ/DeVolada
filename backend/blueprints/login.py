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
__email__ = "marcoorduna1999@cienncias.unam.mx"
__status__ = "Development"

# Instancia al blueprint

login = Blueprint('login',__name__)

"""
Metodo para darle acceso al comprador

return un menaje de si el usuario se registro correctamente, si no, entonces 
manda un mensaje con el error
"""

@login.route('/loginC', methods = ['GET', 'POST'])
def entrarC():
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

"""
Método para darle acceso al vendedor

return un mensaje de si el usario se registró correctamente, si no, manda un mensaje de error
"""

@login.route('/loginV', methods = ['GET', 'POST'])
def entrarV():
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

