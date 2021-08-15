from main import db

__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@ciencias.unam.mx, omar_gramer@ciencias.unam.mx, kethrimtrad@ciencias.unam.mx, karla_dsj@ciencias.unam.mx, antonioreyes21@ciencias.unam.mx"
__status__ = "Development"


class DireccionComprador(db.Model):
    """ Modelo de la tabla direccionComprador de la BD """
    __tablename__ = 'direccionComprador'

    idDir = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), db.ForeignKey('comprador.correo'))
    estado = db.Column(db.String(45))
    ciudad = db.Column(db.String(45))
    colonia = db.Column(db.String(45))
    cp = db.Column(db.Integer)
    calle = db.Column(db.String(45))
    numero = db.Column(db.Integer)

    def __init__(self, correo, estado, ciudad, colonia, cp, calle, numero):
        """
        Inicia la dirección de un comprador ya registrado
        
        Params:
            correo: correo del comprador
            estado: estado
            ciudad: ciudad/municipio
            colonia: colonia
            cp: código postal
            calle: calle
            numero: número
        """
        
        self.correo = correo
        self.estado = estado
        self.ciudad = ciudad
        self.colonia = colonia
        self.cp = cp
        self.calle = calle
        self.numero = numero
