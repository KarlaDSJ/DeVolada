__author__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__copyright__ = "Copyright 2021, Ingenieria de Software "
__credits__ = [""]
__license__ = ""
__version__ = "1.0.2"
__maintainer__ = "Orduña Ávila Marco Antonio, Gramer Muñoz Omar Fernando, Trad Mateos Kethrim Guadalupe, Salas Jiménez Karla Denia, Reyes Martínez Antonio"
__email__ = "marcoorduna1999@cienncias.unam.mx"
__status__ = "Development"


""" 
El archivo config sirve para poder configurar la aplicación
"""

class Config(object):

    # llave secreta para cifrar datos

    SECRET_KEY="my_secret_key"

    # Configuraciones para envíos de correos en compra
    
    MAIL_SERVER ='smtp.gmail.com'
    
    # Puerto para mandar correos

    MAIL_PORT = 465
    
    # Correo para enciar correos de la tienda

    MAIL_USERNAME = 'mercadodevolada@gmail.com'
    
    # contraseña de correo
    
    MAIL_PASSWORD = '7yR9Y5iDhrmXKjG'
    
    # Capa de seguridad de trasporte de correos
    
    MAIL_USE_TLS = False

    # Secure Sockets Layer para mandar correos

    MAIL_USE_SSL = True

class DevelopmentConfig(Config):
    
    # Modo development activado

    DEBUG= True

    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/mydb'
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pruebatest@localhost/mydb'
    
    # Evitar warning de los errores

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    

