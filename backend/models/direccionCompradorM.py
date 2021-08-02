from main import db
from sqlalchemy import relationship

class DireccionComprador(db.Model):
    """Modelo de la tabla direccionComprador de la BD"""
    __tablename__ = 'direccionComprador'
    
    id_dir = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'))
    estado = db.Column(db.String(45))
    ciudad = db.Column(db.String(45))
    colonia = db.Column(db.String(45)) 
    cp = db.Column(db.String(45))
    calle = db.Column(db.String(45)) 
    numero = db.Column(db.String(45))

    def __init__(self, correo, estado, ciudad, colonia, cp, calle, numero):
        self.correo = correo
        self.estado = estado
        self.ciudad = ciudad
        self.colonia = colonia 
        self.cp = cp
        self.calle = calle
        self.numero = numero
