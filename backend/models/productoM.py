from main import db
from models import imagenM

class Producto(db.Model):
    """Modelo de la tabla Producto de la BD"""
    __tablename__ = 'producto'
    idProducto = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), db.ForeignKey('vendedor.correo'))
    precio = db.Column(db.Float)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(500))
    vendidos = db.Column(db.Integer)
    disponibles = db.Column(db.Integer)
    # Relaciones  
    imagenes = db.relationship('Imagen', uselist=False, lazy='select')
    #categoria = db.relationship('Categoria', uselist=False, lazy='select') 

    def __init__(self, correo, precio, nombre, descripcion, vendidos, disponible):
        self.correo = correo
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion 
        self.vendidos = vendidos
        self.disponibles = disponible
