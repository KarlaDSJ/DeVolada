from main import db
from sqlalchemy import ForeignKey
from sqlalchemy import relationship

class Producto(db.Model):
    """Modelo de la tabla Producto de la BD"""
    id_producto = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), ForeignKey('vendedor.correo'))
    precio = db.Column(db.Float)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(100)) #Creo que 100 es poco
    vendidos = db.Column(db.Integer)
    disponibles = db.Column(db.Integer)

    producto = relationship("vendedor")


    def __init__(self, correo, precio, nombre, descripcion, vendidos, disponible):
        self.correo = correo
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion 
        self.vendidos = vendidos
        self.disponibles = disponible
