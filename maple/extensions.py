#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: extensions.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-02 12:35:57 (CST)
# Last Update:星期六 2016-11-5 15:22:15 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request
from flask_socketio import SocketIO
from flask_admin import Admin
from flask_maple import Bootstrap, Captcha, Error
from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager
from redis import StrictRedis
from flask_cache import Cache
from flask_babelex import Babel, Domain
from flask_babelex import lazy_gettext as _
from flask_mail import Mail
from flask_principal import Principal
from flask_sqlalchemy import SQLAlchemy
from flask_avatar import Avatar
from flask_maple.mail import MapleMail
import os


def register_maple(app):
    maple = Bootstrap(
        css=('style/css/honmaple.css', 'style/css/monokai.css'),
        js=('style/js/highlight.js', 'style/js/rain.js'),
        use_auth=True)
    maple.init_app(app)
    Captcha(app)
    Error(app)


class Redis(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        config = app.config
        self._redis_client = StrictRedis(
            db=config['CACHE_REDIS_DB'],
            password=config['CACHE_REDIS_PASSWORD'])

    def __getattr__(self, name):
        return getattr(self._redis_client, name)

    def __getitem__(self, name):
        return self._redis_client[name]

    def __setitem__(self, name, value):
        self._redis_client[name] = value

    def __delitem__(self, name):
        del self._redis_client[name]


def register_login():
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message = _("Please login to access this page.")

    from maple.user.models import User

    @login_manager.user_loader
    def user_loader(id):
        user = User.query.get(int(id))
        return user

    return login_manager


def register_babel():
    translations = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'translations'))
    domain = Domain(translations)
    babel = Babel(default_domain=domain)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(['zh', 'en'])

    @babel.timezoneselector
    def get_timezone():
        return 'UTC'

    return babel


csrf = CsrfProtect()
cache = Cache()
babel = register_babel()
mail = MapleMail()
db = SQLAlchemy()
principals = Principal()
admin = Admin(name='HonMaple', template_mode='bootstrap3')
login_manager = register_login()
redis_data = Redis()
socketio = SocketIO()
avatar = Avatar()
