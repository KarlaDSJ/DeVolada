from enum import unique
from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

# Productos comprados 
class Incluir(db.Model):
    """
    Modelo para la tabla incluir de la base de datos
    """
    __tablename__ = 'incluir'
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'),
                       primary_key=True, nullable=False)  
    idCompra = db.Column(db.Integer, db.ForeignKey('compra.idCompra'),
                        primary_key=True, nullable=False)  
    cantidad = db.Column(db.Integer)

    def __init__ (self, idProducto, idCompra, cantidad):
        """
        Inicia una relación para que un carrito de compras
        contenga un producto
        Params:
            idProducto: identificador del producto
            idCompra: identificador del carrito de compras
            cantidad: cantidad a guardar del producto
        """
        self.idCompra = idCompra
        self.idProducto = idProducto
        self.cantidad = cantidad