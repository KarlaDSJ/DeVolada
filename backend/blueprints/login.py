from flask import Blueprint , render_template
from flask import session
import form
from models.compradorM import Comprador
from flask import flash
from flask import redirect
from flask import url_for
from flask import request

login = Blueprint('login',__name__)

@login.route('/login', methods = ['GET', 'POST'])
def entrar():
    login_form = form.LoginForm(request.form)
    
    if request.method == 'POST' and login_form.validate():
        email = login_form.email.data
        password = login_form.password.data
        comprador = Comprador.query.filter_by(correo = email).first()
        if comprador is not None and comprador.verify_password(password):
            success_message = 'Bienbenido {}'.format(email)
            flash(success_message)
            session['email'] = email
            return redirect(url_for('index.inicio'))

        else: 
            error_message = 'correo o ocntraseña no validas'
            flash(error_message)
        
        session['email'] = login_form.email.data
        print(login_form.email.data)
   
      

    return render_template('login.html', form = login_form)