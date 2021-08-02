from main import db
from sqlalchemy import ForeignKey
# from sqlalchemy import relationship

class Producto(db.Model):
    """Modelo de la tabla Producto de la BD"""
    idProducto = db.Column(db.Integer, primary_key=True, unique=True)
    correo = db.Column(db.String(45), db.ForeignKey('vendedor.correo'), nullable=False)
    precio = db.Column(db.Float)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(100)) #Creo que 100 es poco
    vendidos = db.Column(db.Integer)
    disponibles = db.Column(db.Integer)  

    # Relaciones
    contenido_en = db.relationship('Contener', backref='producto', lazy=True)              


    def __init__(self, correo, precio, nombre, descripcion, vendidos, disponible):
        self.correo = correo
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion 
        self.vendidos = vendidos
        self.disponibles = disponible
