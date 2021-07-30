from flask import Blueprint , render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import request


after = Blueprint('after',__name__)

@after.after_request
def after_request(response):
    return response
