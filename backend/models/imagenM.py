from main import db

class Imagen(db.Model):
    __tablename__ = 'imagen'
    imagen = db.Column(db.String(100), primary_key = True, unique=True)
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'), primary_key = True)

    def __init__(self,imagen,idProducto):
        self.imagen = imagen
        self.idProducto = idProducto