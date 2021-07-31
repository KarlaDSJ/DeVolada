from main import db

class Producto(db.Model):
    idProducto = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.Unicode)
    precio = db.Column(db.Float)
    nombre = db.Column(db.Unicode)
    descripcion = db.Column( db.Unicode)
    vendidos = db.Column(db.Integer)
    disponibles = db.Column(db.Integer)


    def __init__(self, correo, precio, nombre, descripcion, vendidos, disponible):
        self.correo = correo
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion 
        self.vendidos = vendidos
        self.disponibles = disponible
