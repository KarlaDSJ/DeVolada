from main import db

class Imagen(db.Model):
    __tablename__ = 'imagen'
    imagen = db.Column(db.String(45),primary_key = True, unique=True)
    idProducto = db.ForeignKey('imagen.producto'),

    def __init__(self,imagen,idProducto):
        self.imagen = imagen
        self.idProducto = idProducto