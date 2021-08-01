from enum import unique
from main import db

# Productos comprados 
class Incluir(db.Model):
    __tablename__ = 'incluir'
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'),
                       nullable=False)  
    idCompra = db.Column(db.Integer, db.ForeignKey('compra.idCompra'),
                       nullable=False)  
    cantidad = db.Column(db.Integer)
    #Relaciones
    producto = db.relationship('Producto', uselist=False, lazy='select') 

    def __init__ (self, idProducto, idCompra, cantidad):
        self.idCompra = idCompra
        self.idProducto = idProducto
        self.cantidad = cantidad