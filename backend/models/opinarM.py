from models.productoM import Producto
from main import db

class Opinar(db.Model):
    __tablename__ = 'opinar'
    idProducto = db.Column(db.String(45),primary_key = True, unique=True)
    correo = db.Column(db.String(45))
    opinion = db.Column(db.Unicode)
    calificacion = db.Column(db.Integer)
    #Relaciones
    #autor = db.relationship('comprador', back_populates="comprador")
    #producto = db.relationship("producto")

    def __init__(self, correo, opinion, calificacion):
        self.correo = correo
        self.opinion = opinion
        self.calificacion = calificacion
