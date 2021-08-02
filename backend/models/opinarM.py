from backend.models.productoM import Producto
from main import db

class Opinar(db.Model):
    __tablename__ = 'opinar'
    idProducto = db.Column(db.String(45), db.ForeignKey('producto.idProducto'))
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'))
    opinion = db.Column(db.Unicode)
    calificacion = db.Column(db.Integer)
    #Relaciones
    autor = db.relationship('Comprador', back_populates="comprador")
    producto = db.relationship("Producto")

    def __init__(self, correo, opinion, calificacion):
        self.correo = correo
        self.opinion = opinion
        self.calificacion = calificacion
