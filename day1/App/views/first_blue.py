from flask import Blueprint, render_template

from App.models import models

blue = Blueprint('blue',__name__)

@blue.route('/')
def index():
    #return('123')
    return render_template('index.html', msg="这天气适合睡觉")

@blue.route('/createdb/')
def createdb():
    models.create_all()

    return '创建成功'