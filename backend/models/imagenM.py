from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

class Imagen(db.Model):
    __tablename__ = 'imagen'
    idImagen = db.Column(db.Integer, primary_key=True, unique=True)
    imagen = db.Column(db.Text)
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'), primary_key = True)

    def __init__(self,imagen,idProducto):
        """
        Crea una imagen correspondiente a un producto
        
        Params:
            imagen: ruta de la imagen
            idProducto: número del producto
        """
        self.imagen = imagen
        self.idProducto = idProducto