import os

from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SECRET_KEY="my_secret_key"
    # Configuraciones para envíos de correos en compra
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'mercadodevolada@gmail.com'
    MAIL_PASSWORD = '7yR9Y5iDhrmXKjG'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class DevelopmentConfig(Config):
    DEBUG= True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/mydb'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pruebatest@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    

