from main import db
from sqlalchemy import ForeignKey


class TarjetaVendedor(db.Model):
    """Modelo de la tabla tarjetaVendedor de la BD"""
    __tablename__ = 'tarjetaVendedor'
    numero = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), ForeignKey('vendedor.correo'))
   

    def __init__(self, correo, numero):
        self.correo = correo
        self.numero = numero