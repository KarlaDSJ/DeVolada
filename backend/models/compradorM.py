from main import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"


class Comprador(db.Model):
    ''' Modelo para la tabla comprador '''
    __tablename__ = 'comprador'
    correo = db.Column(db.String(45), primary_key=True, unique=True)
    nombre = db.Column(db.Unicode)
    telefono = db.Column(db.String(15))
    contrasenia = db.Column(db.String(105))

     # Relaciones    
    carrito_propio = db.relationship('Pertenecer', backref='comprador', lazy=True)
    tarjeta = db.relationship('TarjetaComprador', backref='duenio', lazy=True)
    

    def __init__(self, correo, nombre, telefono, contrasenia):
        """
        Inicia un comprador
        
        Params:
            correo: correo        
            nombre: nombre    
            telefono: teléfono        
            contrasenia: contraseña
        """
        self.correo = correo
        self.nombre = nombre
        self.telefono = telefono
        self.contrasenia = self.__create_password(contrasenia)

    def __create_password(self, password):
        """
        Hashea la contraseña del comprador actual
        
        Params:
            password: contraseña
        Returns: 
        contraseña hasheada
        """
        return generate_password_hash(password)

    def verify_password(self, password):
        """
        Verifica que la contraseña ingresada coincida con la hasheada
        Params:
            password: contraseña que se desea ingresar
        Returns: booleano indicando si son iguales o no
        """
        return check_password_hash(self.contrasenia, password)
