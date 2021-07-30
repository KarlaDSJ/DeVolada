from flask import Blueprint, render_template, make_response



cookie = Blueprint('cookie',__name__)

@cookie.route('/cookie')
def galleta():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custom_cookie', 'Marco')
    return response

