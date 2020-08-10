from flask import Flask
#from App.views import blue, second
#from flask_sqlalchemy import SQLAlchemy

from App.ext import init_ext
from App.settings import envs
from App.views import init_view


def create_app(env):

    app = Flask(__name__)
    #app.register_blueprint(blue)
    #app.register_blueprint(second)

#    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
#    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:asdf1234qwer@localhost:3306/DAY2FLASK"
#    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(envs.get(env))

    init_ext(app)

    init_view(app = app)

    return app
