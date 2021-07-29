from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

from flask_wtf.csrf import CsrfProtect
from config import DevelopmentConfig
from blueprints.productos import producto
from blueprints.index import index
from blueprints.login import login
from blueprints.create import create
from blueprints.logout import logout
from blueprints.before import before
from blueprints.after import after
from blueprints.cookie import cookie

app = Flask(__name__)
csrf = CsrfProtect()

app.config.from_object(DevelopmentConfig)


app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(create)
app.register_blueprint(logout)
#app.register_blueprint(before)
app.register_blueprint(after)
app.register_blueprint(cookie)
db.init_app(app)
csrf.init_app(app)
app.run(port=7000)
if __name__ == '__main__':

   
    
    with app.app_context():
        db.create_all()
        ma.init_app(app)

    
