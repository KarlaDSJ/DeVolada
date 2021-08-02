from main import db

# Productos contenidos en un carrito
class Contener(db.Model):
    __tablename__ = 'contener'
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'),
                       nullable=False, primary_key=True, unique=True)  
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False, primary_key=True, unique=True)  
    cantidad = db.Column(db.Integer)
    #Relaciones
    productos = db.relationship('producto') 

    def __init__ (self, idProducto, idCarrito, cantidad):
        self.idCarrito = idCarrito
        self.idProducto = idProducto
        self.cantidad = cantidad