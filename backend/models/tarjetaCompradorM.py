from main import db
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"


def generar_codigo( item):
    """
    Genera un nuevo código para la tarjeta usando cifrado Caesar
    Params:
        item: número de tarjeta
    Returns: número de tarjeta codificado
    """
    nuevo = ""
    for i in range(0,len(item),1):
        nuevo+=str(  (int(item[i])+3)  %  10)
    return nuevo


class TarjetaComprador(db.Model):
    """ Modelo de la tabla tarjetaComprador de la BD """
    __tablename__ = 'tarjetaComprador'
    numero = db.Column(db.String(16), primary_key=True)
    correo = db.Column(db.String(45), ForeignKey('comprador.correo'), primary_key=True)
    dueno = db.Column(db.String(45))
    fechaCad = db.Column(db.Date)
    cvv = db.Column(db.String(105)) 

    def __init__(self, correo, numero, dueno, fechaCad, cvv):
        """
        Inicia una tarjeta para algún comprador ya registrado
        Params:
            correo: correo del comprador
            numero: número de tarjeta en formato string
            dueno: nombre del titular de la tarjeta
            fechaCad: fecha de caducidad
            cvv: código de seguridad
        """
        self.correo = correo
        self.dueno = dueno
        self.fechaCad = fechaCad 
        self.cvv = self.guardar_codigo(cvv)
        self.numero = generar_codigo(numero)

    def guardar_codigo(self,item):
        """
        Guarda el código de seguridad de la tarjeta hasheado
        Params:
            item: código de seguridad
        Returns: llave hash del código
        """
        return generate_password_hash(item)

