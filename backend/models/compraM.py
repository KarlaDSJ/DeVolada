from enum import unique
from main import db


# Registro de la compra finalizada
class Compra (db.Model):
    __tablename__ = 'compra'
    idCompra = db.Column(db.Integer, primary_key=True, unique=True)
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'), 
                        db.ForeignKey('direccionComprador.correo'),
                        db.ForeignKey('tarjetaComprador.correo'))
    idDir = db.Column(db.Integer, db.ForeignKey('direccionComprador.idDir'))
    numero = db.Column(db.String(45), db.ForeignKey('tarjetaComprador.numero')) 
    total = db.Column(db.Float)
    # Relaciones    
    productos_comprados = db.relationship('Incluir', backref='compra', lazy='select')


    def __init__ (self, correo, idDir, tarjeta, total):
        self.correo = correo
        self.idDir = idDir
        self.numero = tarjeta
        self.total = total