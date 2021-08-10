from main import db


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
