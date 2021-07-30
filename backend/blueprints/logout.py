from flask import Blueprint
from flask import session
from flask import redirect
from flask import url_for

logout = Blueprint('logout',__name__)

@logout.route('/logout')
def salir():
    if 'email' in session:
        session.pop('email')
    return redirect(url_for('login.entrar'))