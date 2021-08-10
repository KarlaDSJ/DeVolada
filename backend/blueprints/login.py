from models.vendedorM import Vendedor
from flask import Blueprint
from flask import session
from flask.json import jsonify
from models.compradorM import Comprador
from flask import request

login = Blueprint('login',__name__)

@login.route('/loginC', methods = ['GET', 'POST'])
def entrarC():
    correo = request.json['correoC']
    contrasenia = request.json['contraseniaC']
    comprador = Comprador.query.filter_by(correo = correo).first()
    

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
    correo = request.json['correoV']
    contrasenia = request.json['contraseniaV']
    
    vendedor = Vendedor.query.filter_by(correo = correo).first()
   

    if (vendedor is not None ):
        if (vendedor.correo == correo and vendedor.verify_password(contrasenia) ):
            session['email'] = correo
            sesionActiva = session['email']
            return jsonify({'msg':'success','session':sesionActiva, 'nombre': vendedor.nombre })
        else: 
            return jsonify({'msg': 'error_contrasenia'})
    else:
        return jsonify({'msg': 'error_datos'})