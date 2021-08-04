from flask import Blueprint
from flask import session
from flask import redirect
from flask import url_for
from flask.json import jsonify

logout = Blueprint('logout',__name__)

@logout.route('/logout')
def salir():
    if 'email' in session:
        session.pop('email')
    return jsonify({'msg':'bien'})