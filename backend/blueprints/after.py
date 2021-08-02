from flask import Blueprint
from flask import session
from flask import request


after = Blueprint('after',__name__)

@after.after_request
def after_request(response):
    return response
