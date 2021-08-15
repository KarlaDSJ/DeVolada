from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"


# Productos en el carrito
class Pertenecer (db.Model):
    """
    Modelo de la tabla pertenecer de la base de datps
    """
    __tablename__ = 'pertenecer'
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'),
                       nullable=False, primary_key=True, unique=True)
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False, primary_key=True, unique=True)

    def __init__ (self, correo, idCarrito):
        """
        Inicia una relación entre un comprador y un carrito de compras
        Params:
            correo: correo del comprador
            idCarrito: identificador del carrito de compras
        """
        self.correo = correo
        self.idCarrito = idCarrito



