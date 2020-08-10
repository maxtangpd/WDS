from flask import Blueprint, render_template

from App.models import models, User

blue = Blueprint('blue',__name__)

@blue.route('/')
def index():
    #return('123')
    return render_template('index.html', msg="这天气适合睡觉")

@blue.route('/createdb/')
def createdb():
    models.create_all()

    return '创建成功'

@blue.route('/dropdb')
def dropdb():
    models.drop_all()

    return '删除成功'

@blue.route('/adduser')
def add_user():
    user = User()
    user.username = "TOM"
    user.save()
#    models.session.add(user)
#    models.session.commit()

    return '创建成功'