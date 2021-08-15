from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

class Categoria(db.Model):
    __tablename__ = 'categoria'
    categoria = db.Column(db.String(45),primary_key = True, unique=True)
    idProducto = db.Column(db.Integer,db.ForeignKey('producto.idProducto'), primary_key = True)

    def __init__(self,categoria,idProducto):
        """
        Inicia una categoría de un producto
        
        Params:
            categoria: nombre de la categoría        
            idProducto: identificador del producto   
        """

        self.categoria = categoria
        self.idProducto = idProducto