from main import db
"""Importamos los modelos para que no cause error las relaciones"""
from models import imagenM
from models import categoriaM
from models.contenerM import Contener

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"

class Producto(db.Model):
    """Modelo de la tabla Producto de la BD"""
    __tablename__ = 'producto'
    idProducto = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), db.ForeignKey('vendedor.correo'), nullable=False)
    precio = db.Column(db.Float)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(500))
    vendidos    = db.Column(db.Integer)
    disponibles = db.Column(db.Integer)

    # Relaciones (harán el join cuando seleccionemos los productos)
    imagenes  = db.relationship('Imagen',    cascade="all, delete-orphan", lazy='select')
    categoria = db.relationship('Categoria', cascade="all, delete-orphan", lazy='select')
    incluir   = db.relationship('Incluir',   cascade="all, delete-orphan")
    contener  = db.relationship('Contener',  cascade="all, delete-orphan")

    def __init__(self, correo, precio, nombre, descripcion, vendidos, disponible):
        """
        Crea un producto
        
        Params:
            correo: correo del vendedor  
            precio: precio del producto     
            nombre: nombre del producto  
            descripcion: descripción        
            vendidos: número de productos vendidos
            disponibles: número de productos disponibles
        """

        self.correo = correo
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion 
        self.vendidos = vendidos
        self.disponibles = disponible
