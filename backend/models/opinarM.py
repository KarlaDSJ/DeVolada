from models.productoM import Producto
from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"


class Opinar(db.Model):
    __tablename__ = 'opinar'
    idProducto = db.Column(db.String(45),db.ForeignKey('producto.idProducto'),primary_key = True, unique=True)
    correo = db.Column(db.String(45),db.ForeignKey('comprador.correo'), primary_key = True, unique=True)
    opinion = db.Column(db.Unicode)
    calificacion = db.Column(db.Integer)
    #Relaciones
    #autor = db.relationship('comprador', back_populates="comprador")
    #producto = db.relationship("producto")

    def __init__(self, correo, idProducto, opinion, calificacion):
        """
        Crea una reseña y la asocia a un producto
        Params:
            idProducto: identificador del producto
            correo: identificador del comprador
            opinion: opinión del producto
            calificacion: calificación dada al producto
        """
        self.correo = correo
        self.idProducto = idProducto
        self.opinion = opinion
        self.calificacion = calificacion