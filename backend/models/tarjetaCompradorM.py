from main import db
<<<<<<< HEAD
from sqlalchemy import ForeignKey
from sqlalchemy import relationship

class TarjetaComprador(db.Model):
    """Modelo de la tabla tarjetaComprador de la BD"""

    numero = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), ForeignKey('comprador.correo'))
=======

class TarjetaComprador(db.Model):
    """Modelo de la tabla tarjetaComprador de la BD"""
    __tablename__ = 'tarjetaComprador'
    numero = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'))
>>>>>>> a5a7f809551d442cb8ba157caa045dd862a2aa8f
    duenio = db.Column(db.String(45))
    fechCad = db.Column(db.Date)
    cvv = db.Column(db.Integer) 

<<<<<<< HEAD
    # tarjeta = relationship("comprador")


=======
>>>>>>> a5a7f809551d442cb8ba157caa045dd862a2aa8f
    def __init__(self, correo, numero, duenio, fechCad, cvv):
        self.correo = correo
        self.numero = numero
        self.duenio = duenio
        self.fechCad = fechCad 
        self.cvv = cvv
