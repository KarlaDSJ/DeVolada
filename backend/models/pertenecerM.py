from main import db

# Productos en el carrito
class Pertenecer (db.Model):
    __tablename__ = 'pertenecer'
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'),
                       nullable=False)
    idCarrito = db.Column(db.Integer, db.ForeignKey('carrito.idCarrito'),
                       nullable=False)
    #Relaciones
    comprador = db.relationship('Comprador', back_populates='comprador')
    carrito = db.relationship('Carrito', back_populates='carrito')
    
    def __init__ (self, correo, idCarrito):
        self.correo = correo
        self.idCarrito = idCarrito