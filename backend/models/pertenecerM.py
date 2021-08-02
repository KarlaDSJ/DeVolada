from main import db
from enum import unique
# Productos en el carrito
class Pertenecer(db.Model):
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'),
                       nullable=False, primary_key=True, unique=True)
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False, primary_key=True, unique=True)

    def __init__ (self, correo, idCarrito):
        self.correo = correo
        self.idCarrito = idCarrito



