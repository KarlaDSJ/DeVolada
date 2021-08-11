from main import db


# Productos en el carrito
class Pertenecer (db.Model):
    """
    Modelo de la tabla pertenecer de la base de datps
    """
    __tablename__ = 'pertenecer'
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'),
                       nullable=False, primary_key=True, unique=True)
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False, primary_key=True, unique=True)

    def __init__ (self, correo, idCarrito):
        """
        Inicia una relación entre un comprador y un carrito de compras
        Params:
            correo: correo del comprador
            idCarrito: identificador del carrito de compras
        """
        self.correo = correo
        self.idCarrito = idCarrito



