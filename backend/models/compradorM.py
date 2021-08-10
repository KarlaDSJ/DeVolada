from main import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class Comprador(db.Model):
    __tablename__ = 'comprador'
    correo = db.Column(db.String(45),primary_key=True, unique=True)
    nombre = db.Column(db.Unicode)
    telefono = db.Column(db.String(15))
    contrasenia = db.Column(db.String(105))
    # Relaciones    
    carrito_propio = db.relationship('Pertenecer', backref='comprador', lazy=True)
    tarjeta = db.relationship('TarjetaComprador', backref='duenio', lazy=True)

    

    def __init__(self,correo, nombre,telefono,contrasenia):
        self.correo = correo
        self.nombre = nombre
        self.telefono = telefono
        self.contrasenia = self.__create_password(contrasenia)

    def __create_password(self,password):
        return generate_password_hash(password) 

    def verify_password(self, password):
        return check_password_hash(self.contrasenia, password)

  

