from flask import Blueprint

usr = Blueprint('usr',__name__)

@usr.route('/list')
def list():
    return 'list'

@usr.route('/detail')
def detail():
    return 'detail'