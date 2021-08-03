from enum import unique
from main import db

# Productos comprados 
class Incluir(db.Model):
    __tablename__ = 'incluir'
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'),
                       primary_key=True, nullable=False)  
    idCompra = db.Column(db.Integer, db.ForeignKey('compra.idCompra'),
                        primary_key=True, nullable=False)  
    cantidad = db.Column(db.Integer)

    def __init__ (self, idProducto, idCompra, cantidad):
        self.idCompra = idCompra
        self.idProducto = idProducto
        self.cantidad = cantidad