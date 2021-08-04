import os

from flask_sqlalchemy import SQLAlchemy

class Config(object):
    SECRET_KEY="my_secret_key"

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    

