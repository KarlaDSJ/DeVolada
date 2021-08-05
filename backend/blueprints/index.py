from flask import Blueprint , render_template
from flask import session

index = Blueprint('index',__name__)

@index.route('/')
def inicio():
    return render_template('index.html') 
