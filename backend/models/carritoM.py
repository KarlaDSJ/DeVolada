from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"


# Carrito de compras
class Carrito (db.Model):
    """ Modelo de la tabla carrito de la base de datos """
    __tablename__ = 'carrito'
    idCarrito = db.Column(db.Integer, primary_key=True, unique=True)

    # Relaciones
    pertenece_a = db.relationship('Pertenecer', backref='carrito', lazy=True)
    productos = db.relationship('Contener', backref='carrito', lazy=True)