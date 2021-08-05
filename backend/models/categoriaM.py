from main import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    categoria = db.Column(db.String(45),primary_key = True, unique=True)
    idProducto = db.Column(db.Integer,db.ForeignKey('producto.idProducto'), primary_key = True)

    def __init__(self,categoria,idProducto):
        self.categoria = categoria
        self.idProducto = idProducto