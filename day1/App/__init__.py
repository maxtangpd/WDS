from flask import Flask
#from App.views import blue, second
from flask_sqlalchemy import SQLAlchemy


from App.models import init_model
from App.views import init_view


def create_app():

    app = Flask(__name__)
    #app.register_blueprint(blue)
    #app.register_blueprint(second)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_model(app)

    init_view(app = app)

    return app

