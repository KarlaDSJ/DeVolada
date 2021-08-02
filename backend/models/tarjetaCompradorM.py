from main import db
from sqlalchemy import ForeignKey
from sqlalchemy import relationship

class TarjetaComprador(db.Model):
    """Modelo de la tabla tarjetaComprador de la BD"""

    numero = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), ForeignKey('comprador.correo'))
    duenio = db.Column(db.String(45))
    fechCad = db.Column(db.Date)
    cvv = db.Column(db.Integer) 

    # tarjeta = relationship("comprador")


    def __init__(self, correo, numero, duenio, fechCad, cvv):
        self.correo = correo
        self.numero = numero
        self.duenio = duenio
        self.fechCad = fechCad 
        self.cvv = cvv
