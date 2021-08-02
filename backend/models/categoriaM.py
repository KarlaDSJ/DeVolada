from main import db

class Categoria(db.Model):
    __tablename__ = 'categoria'
    categoria  = db.Column(db.String(45),primary_key = True, unique=True)
    idProducto = db.ForeignKey('categoria.producto'),

    def __init__(self,categoria,idProducto):
        self.categoria = categoria
        self.idProducto = idProducto