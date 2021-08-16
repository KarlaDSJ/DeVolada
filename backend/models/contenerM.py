from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

# Productos contenidos en un carrito
class Contener(db.Model):
    """ Modelo de la tabla contener de la base de datos """
    __tablename__ = 'contener'
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'),
                       nullable=False, primary_key=True, unique=True)  
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False, primary_key=True, unique=True)  
    cantidad = db.Column(db.Integer)

    def __init__ (self, idProducto, idCarrito, cantidad):
        """
        Inicia una relación entre una compra y un producto que se compró en ella
        Params:
            idProducto: identificador del producto comprado
            idCarrito: identificador del carrito de compras
            cantidad: cantidad comprada del producto
        """
        self.idCarrito = idCarrito
        self.idProducto = idProducto
        self.cantidad = cantidad