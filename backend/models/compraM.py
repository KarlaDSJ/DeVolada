from enum import unique
from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"


# Registro de la compra finalizada
class Compra (db.Model):
    __tablename__ = 'compra'
    idCompra = db.Column(db.Integer, primary_key=True, unique=True)
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'), 
                        db.ForeignKey('direccionComprador.correo'),
                        db.ForeignKey('tarjetaComprador.correo'))
    idDir = db.Column(db.Integer, db.ForeignKey('direccionComprador.idDir'))
    numero = db.Column(db.String(45), db.ForeignKey('tarjetaComprador.numero')) 
    total = db.Column(db.Float)
    # Relaciones    
    productos_comprados = db.relationship('Incluir', backref='compra', lazy='select')


    def __init__ (self, correo, idDir, tarjeta, total):
        """
        Crea los datos para una compra 
        
        Params:
            correo: correo del comprador      
            idDir: identificador del correo del comprador    
            numero: identificador de la tarjeta del comprador       
            total: total a pagar en la compra
        """
        self.correo = correo
        self.idDir = idDir
        self.numero = tarjeta
        self.total = total