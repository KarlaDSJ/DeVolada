from main import db
from sqlalchemy import ForeignKey

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"


class TarjetaVendedor(db.Model):
    """Modelo de la tabla tarjetaVendedor de la BD"""
    __tablename__ = 'tarjetaVendedor'
    numero = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), ForeignKey('vendedor.correo'))
   

    def __init__(self, correo, numero):
        """
        Inicia una tarjeta para un vendedor
        Params:
            correo: correo del vendedor
            numero: número de tarjeta en formato string
        """

        self.correo = correo
        self.numero = numero