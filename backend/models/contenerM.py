from main import db

# Productos contenidos en un carrito
class Contener(db.Model):
    """ Modelo de la tabla contener de la base de datos """
    __tablename__ = 'contener'
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'),
                       nullable=False, primary_key=True, unique=True)  
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False, primary_key=True, unique=True)  
    cantidad = db.Column(db.Integer)

    def __init__ (self, idProducto, idCarrito, cantidad):
        """
        Inicia una relación entre una compra y un producto que se compró en ella
        Params:
            idProducto: identificador del producto comprado
            idCarrito: identificador del carrito de compras
            cantidad: cantidad comprada del producto
        """
        self.idCarrito = idCarrito
        self.idProducto = idProducto
        self.cantidad = cantidad