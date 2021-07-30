from flask import Blueprint , render_template
from flask import session

index = Blueprint('index',__name__)

@index.route('/')
def inicio():
    if 'email'in session:
        email  =session['email']
        print (email)
    title = "Prueba login"
    return render_template('index.html', title = title) 
