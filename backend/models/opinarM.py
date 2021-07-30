from main import db

class Opinar(db.model):
    __tablename__ = 'opinar'
    idProducto = db.Column(str(45),primary_key = True, unique=True)



