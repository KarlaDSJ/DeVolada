from enum import unique
from main import db


# Registro de la compra finalizada
class Compra (db.Model):
    idCompra = db.Column(db.Integer, primary_key=True, unique=True)
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'),
                       db.ForeignKey('direccionComprador.correo'),
                       db.ForeignKey('tarjetaComprador.correo'),
                       nullable=False)
    idDir = db.Column(db.Integer, db.ForeignKey('direccionComprador.idDir'))
    tarjeta = db.Column(db.String(45), db.ForeignKey('tarjetaComprador.numero'),
                       nullable=False)  

    # Relaciones
    productos_comprados = db.relationship('Incluir', backref='compra', lazy=True)


    def __init__ (self, correo, idDir, tarjeta):
        self.correo = correo
        self.idDir = idDir
        self.tarjeta = tarjeta