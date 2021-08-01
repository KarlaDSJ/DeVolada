from main import db
from sqlalchemy import ForeignKey
from sqlalchemy import relationship

class TarjetaVendedor(db.Model):
    """Modelo de la tabla tarjetaVendedor de la BD"""
    __tablename__ = 'tarjetaVendedor'
    numero = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), ForeignKey('vendedor.correo'))
    duenio = db.Column(db.String(45))
    fechCad = db.Column(db.Date)
    cvv = db.Column(db.Integer) 

    def __init__(self, correo, numero, duenio, fechCad, cvv):
        self.correo = correo
        self.numero = numero
        self.duenio = duenio
        self.fechCad = fechCad 
        self.cvv = cvv
