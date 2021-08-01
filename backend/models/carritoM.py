from main import db
from enum import unique

# Carrito de compras 
class Carrito (db.Model):
    idCarrito = db.Column(db.Integer, primary_key=True, unique=True)
    # Relaciones
    pertenece_a = db.relationship('Pertenecer', backref='carrito', lazy=True)        