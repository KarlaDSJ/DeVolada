from enum import unique
from main import db

# Productos contenidos en un carrito
class Contener(db.Model):
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'),
                       nullable=False)  
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False)  
    cantidad = db.Column(db.Integer)

    def __init__ (self, idProducto, idCarrito, cantidad):
        self.idCarrito = idCarrito
        self.idProducto = idProducto
        self.cantidad = cantidad