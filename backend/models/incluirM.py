from enum import unique
from main import db

# Productos comprados 
class Incluir(db.Model):
    """
    Modelo para la tabla incluir de la base de datos
    """
    __tablename__ = 'incluir'
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'),
                       primary_key=True, nullable=False)  
    idCompra = db.Column(db.Integer, db.ForeignKey('compra.idCompra'),
                        primary_key=True, nullable=False)  
    cantidad = db.Column(db.Integer)

    def __init__ (self, idProducto, idCompra, cantidad):
        """
        Inicia una relación para que un carrito de compras
        contenga un producto
        Params:
            idProducto: identificador del producto
            idCompra: identificador del carrito de compras
            cantidad: cantidad a guardar del producto
        """
        self.idCompra = idCompra
        self.idProducto = idProducto
        self.cantidad = cantidad