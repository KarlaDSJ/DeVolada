from main import db
from enum import unique


# Carrito de compras 
class Carrito (db.Model):
    __tablename__ = 'carrito'
    idCarrito = db.Column(db.Integer, primary_key=True,  unique=True)
    # Relaciones
    productos = db.relationship('Pertenecer', back_populates='pertenecer')
    productos = db.relationship('Contener')


    def __init__ (self):
        pass