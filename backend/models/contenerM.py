from main import db

# Productos contenidos en un carrito
class Contener(db.Model):
    __tablename__ = 'contener'
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'),
                       nullable=False)  
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False)  
    cantidad = db.Column(db.Integer)
    #Relaciones
    productos = db.relationship('Producto') 

    def __init__ (self, idProducto, idCarrito, cantidad):
        self.idCarrito = idCarrito
        self.idProducto = idProducto
        self.cantidad = cantidad