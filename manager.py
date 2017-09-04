# !/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: db_create.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-02-11 13:34:38
# *************************************************************************
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from maple import create_app
from maple.extensions import db, cache
from maple.models import User
from getpass import getpass
from werkzeug.security import generate_password_hash
from datetime import datetime
import os

app = create_app('config')
migrate = Migrate(app, db)
manager = Manager(app)


@manager.command
def runserver():
    return app.run()


@manager.command
def publish():
    import requests
    url = 'http://127.0.0.1:8000/blog'
    data = {'title': '1', 'content': '* 1\n** 2 assaaaaa啊啊啊', 'category': '11', 'tags': '11'}
    headers = {'Token': 'Imhvbm1hcGxlIg.DI52VA.QIZAor5LoBUEK5ae0h-MuwccJrQ'}
    response = requests.post(url, data=data, headers=headers)
    return response.text


@manager.command
def clear_cache():
    with app.app_context():
        cache.clear()

# @manager.option('-u', '--user_id', dest='user_id')
# def token(user_id):
#     user_id = int(user_id)
#     return User.query.get(user_id).token


@manager.option('-u', '--username', dest='username')
def token(username):
    return User.query.filter_by(username=username).first().token


@manager.command
def tags():
    '''
    删除重复tags
    '''
    from maple.blog.models import Tags
    tags = Tags.query.distinct(Tags.name).all()
    for tag in tags:
        other_repeat = Tags.query.filter(Tags.name == tag.name,
                                         Tags.id != tag.id).all()
        if other_repeat:
            y_blogs = tag.blogs.all()
            x_blogs = []
            print('当前Tags', tag)
            print('原Blogs', y_blogs)
            for other_repeat_tag in other_repeat:
                x_blogs += other_repeat_tag.blogs.all()
                other_repeat_tag.delete()
            print('重复Blogs', x_blogs)
            blogs = y_blogs + x_blogs
            tag.blogs = blogs
            tag.save()


@manager.command
def init_db():
    """
    Drops and re-creates the SQL schema
    """
    # db.drop_all()
    # db.configure_mappers()
    db.create_all()
    db.session.commit()


@manager.command
def babel_init():
    pybabel = 'pybabel'
    os.system(pybabel +
              ' extract -F babel.cfg -k lazy_gettext -o messages.pot maple')
    os.system(pybabel + ' init -i messages.pot -d translations -l zh')
    os.unlink('messages.pot')


@manager.command
def babel_update():
    pybabel = 'pybabel'
    os.system(
        pybabel +
        ' extract -F babel.cfg -k lazy_gettext -o messages.pot maple templates')
    os.system(pybabel + ' update -i messages.pot -d translations')
    os.unlink('messages.pot')


@manager.command
def babel_compile():
    pybabel = 'pybabel'
    os.system(pybabel + ' compile -d translations')


@manager.option('-u', '--username', dest='username')
@manager.option('-e', '--email', dest='email')
@manager.option('-w', '--password', dest='password')
def create_user(username, email, password):
    if username is None:
        username = input('Username(default admin):') or 'admin'
    if email is None:
        email = input('Email:')
    if password is None:
        password = getpass('Password:')
    user = User()
    user.username = username
    user.password = generate_password_hash(password)
    user.email = email
    user.is_superuser = True
    user.is_confirmed = True
    user.roles = 'Super'
    user.confirmed_time = datetime.utcnow()
    db.session.add(user)
    db.session.commit()


@manager.option('-h', '--host', dest='host', default='127.0.0.1')
@manager.option('-p', '--port', dest='port', type=int, default=8000)
@manager.option('-w', '--workers', dest='workers', type=int, default=2)
def gunicorn(host, port, workers):
    """use gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {'bind': '{0}:{1}'.format(host, port), 'workers': workers}

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
