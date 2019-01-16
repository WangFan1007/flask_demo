from flask import Blueprint

odr = Blueprint('odr',__name__)

@odr.route('/list')
def list():
    return 'odrlist'

@odr.route('/detail')
def detail():
    return 'odrdetail'