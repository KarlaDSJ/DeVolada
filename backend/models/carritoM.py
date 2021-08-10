from main import db


# Carrito de compras
class Carrito (db.Model):
    """ Modelo de la tabla carrito de la base de datos """
    __tablename__ = 'carrito'
    idCarrito = db.Column(db.Integer, primary_key=True, unique=True)
    # Relaciones
    pertenece_a = db.relationship('Pertenecer', backref='carrito', lazy=True)
    productos = db.relationship('Contener', backref='carrito', lazy=True)
