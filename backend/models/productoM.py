from main import db
"""Importamos los modelos para que no cause error las relaciones"""
from models import imagenM
from models import categoriaM

class Producto(db.Model):
    """Modelo de la tabla Producto de la BD"""
    __tablename__ = 'producto'
    idProducto = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), db.ForeignKey('vendedor.correo'), nullable=False)
    precio = db.Column(db.Float)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(500))
    vendidos = db.Column(db.Integer)
    disponibles = db.Column(db.Integer)
    # Relaciones (harán el join cuando seleccionemos los productos)
    imagenes = db.relationship('imagen', lazy='select')
    #categoria = db.relationship('categoria',lazy='select') 
    #contenido_en = db.relationship('contener', backref='producto', lazy=True)              

    def __init__(self, correo, precio, nombre, descripcion, vendidos, disponible):
        self.correo = correo
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion 
        self.vendidos = vendidos
        self.disponibles = disponible
