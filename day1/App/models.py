from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()

def init_model(app):
    models.init_app(app)


class User(models.Model):
    id = models.Column(models.Integer, primary_key = True)
    username = models.Column(models.String(16))