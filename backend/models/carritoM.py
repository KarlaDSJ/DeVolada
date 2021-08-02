from main import db
from enum import unique

# Carrito de compras 
class Carrito (db.Model):
    __tablename__ = 'carrito'
    idCarrito = db.Column(db.Integer, primary_key=True, unique=True)
    # Relaciones
    pertenece_a = db.relationship('pertenecer', backref='carrito', lazy=True)        
    productos = db.relationship('contener', backref='carrito', lazy=True)        

