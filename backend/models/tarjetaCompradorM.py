from main import db
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

def generar_codigo( item):
    nuevo = ""
    for i in range(0,len(item),1):
        nuevo+=str(  (int(item[i])+3)  %  10)
    return nuevo


class TarjetaComprador(db.Model):
    """Modelo de la tabla tarjetaComprador de la BD"""
    __tablename__ = 'tarjetaComprador'
    numero = db.Column(db.String(16), primary_key=True)
    correo = db.Column(db.String(45), ForeignKey('comprador.correo'), primary_key=True)
    dueno = db.Column(db.String(45))
    fechaCad = db.Column(db.Date)
    cvv = db.Column(db.String(105)) 

    def __init__(self, correo, numero, dueno, fechaCad, cvv):
        self.correo = correo
        self.dueno = dueno
        self.fechaCad = fechaCad 
        self.cvv = self.guardar_codigo(cvv)
        self.numero = generar_codigo(numero)

    def guardar_codigo(self,item):
        return generate_password_hash(item)     

# 1563 -> 4896
# 0497 -> 3720
# 0 -> 3
# 1 -> 4
# 2 -> 5
# 3 -> 6
# 4 -> 7
# 5 -> 8
# 6 -> 9
# 7 -> 0
# 8 -> 1
# 9 -> 2    

