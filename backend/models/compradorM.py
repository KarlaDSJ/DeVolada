from main import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class Comprador(db.Model):
    ''' Modelo para la tabla comprador '''
    __tablename__ = 'comprador'
    correo = db.Column(db.String(45), primary_key=True, unique=True)
    nombre = db.Column(db.Unicode)
    telefono = db.Column(db.String(15))
    contrasenia = db.Column(db.String(105))

    def __init__(self, correo, nombre, telefono, contrasenia):
        """
        Inicia un comprador
        
        Params:
            correo: correo        
            nombre: nombre    
            telefono: teléfono        
            contrasenia: contraseña
        """
        self.correo = correo
        self.nombre = nombre
        self.telefono = telefono
        self.contrasenia = self.__create_password(contrasenia)

    def __create_password(self, password):
        """
        Hashea la contraseña del comprador actual
        
        Params:
            password: contraseña
        Returns: 
        contraseña hasheada
        """
        return generate_password_hash(password)

    def verify_password(self, password):
        """
        Verifica que la contraseña ingresada coincida con la hasheada
        Params:
            password: contraseña que se desea ingresar
        Returns: booleano indicando si son iguales o no
        """
        return check_password_hash(self.contrasenia, password)
