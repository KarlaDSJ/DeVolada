from enum import unique
from main import db

# Productos comprados 
class Incluir(db.Model):
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'),
                       nullable=False)  
    idCompra = db.Column(db.Integer, db.ForeignKey('compra.idCompra'),
                       nullable=False)  
    cantidad = db.Column(db.Integer)

    def __init__ (self, idProducto, idCompra, cantidad):
        self.idCompra = idCompra
        self.idProducto = idProducto
        self.cantidad = cantidad