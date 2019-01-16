from flask import Flask

from .views.account import ac
from .views.user import usr
from .views.order import odr

def create_app():
    app = Flask(__name__)
    app.register_blueprint(ac)
    app.register_blueprint(usr)
    app.register_blueprint(odr)
    return app