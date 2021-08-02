from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import session
from flask import request



before = Blueprint('before',__name__)

@before.before_request
def before_request():
    if 'email' not in session and request.endpoint not in['login.entrar','create.crear']  :
       redirect(url_for('login.entrar'))
    elif 'email' in session and request.endpoint in ['login.entrar','create.crear']:
        return redirect(url_for('index.inicio'))