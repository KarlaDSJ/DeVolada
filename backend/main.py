from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
"""



from blueprints.after import after
from blueprints.cookie import cookie
from blueprints.imagen import imagen
from blueprints.categoria import categoria
from blueprints.createResena import createResena
from blueprints.showResenas import showResenas
#from blueprints.before import before
# from blueprints.adminProducto import adminProducto


# Mis blueprints"""
from blueprints.logout import logout
from blueprints.create import create
from blueprints.productos import producto
from blueprints.comprador import comprador
from blueprints.vendedor import vendedor
from blueprints.login import login
from blueprints.index import index
"""from blueprints.carrito import carrito
from blueprints.pertenecer import pertenecer
from blueprints.contener import contener"""
from flask_mail import Mail

app = Flask(__name__)
csrf = CSRFProtect()
CORS(app)

app.config.from_object(DevelopmentConfig)
mail = Mail()
mail.init_app(app)

app.register_blueprint(comprador)
app.register_blueprint(vendedor)
app.register_blueprint(producto)
app.register_blueprint(login)
app.register_blueprint(index)
app.register_blueprint(create)
app.register_blueprint(logout)
"""app.register_blueprint(carrito)
app.register_blueprint(pertenecer)
app.register_blueprint(contener)


# Ya estaban 




app.register_blueprint(after)
app.register_blueprint(cookie)
app.register_blueprint(imagen)
app.register_blueprint(categoria)
app.register_blueprint(createResena)
app.register_blueprint(showResenas)"""
#app.register_blueprint(before)
# app.register_blueprint(adminProducto)



db.init_app(app)
# Lo comenté porque necesitaba iniciar sesión para hacer peticiones
# csrf.init_app(app)







if __name__ == '__main__':
    app.run(port=7000)    
    
    with app.app_context():
        db.create_all()
        ma.init_app(app)

    
