from enum import unique
from main import db


# Registro de la compra finalizada
class Compra (db.Model):
    __tablename__ = 'compra'
    idCompra = db.Column(db.Integer, primary_key=True, unique=True)
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'))
    idDir = db.Column(db.Integer, db.ForeignKey('direccionComprador.idDir'))
    tarjeta = db.Column(db.String(45), db.ForeignKey('tarjetaComprador.numero'))  
    # Relaciones
    productos_comprados = db.relationship('Incluir', uselist=False, lazy='select')


    def __init__ (self, correo, idDir, tarjeta):
        self.correo = correo
        self.idDir = idDir
        self.tarjeta = tarjeta