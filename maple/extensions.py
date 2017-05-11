#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: extensions.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-02 12:35:57 (CST)
# Last Update:星期四 2017-5-11 16:44:3 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request
from flask_admin import Admin
from flask_maple import Bootstrap, Captcha, Error
from flask_maple.redis import Redis
from flask_maple.mail import Mail
from flask_maple.middleware import Middleware
from flask_maple.app import App
from flask_maple.json import CustomJSONEncoder
from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager
from flask_cache import Cache
from flask_babelex import Babel, Domain
from flask_babelex import lazy_gettext as _
from flask_maple.models import db
import os


def register_maple(app):
    maple = Bootstrap(
        css=('dist/css/honmaple.css', 'dist/css/monokai.css'),
        js=('dist/js/highlight.js', 'dist/js/rain.js', 'dist/js/org.js'),
        use_auth=False)
    maple.init_app(app)
    Captcha(app)
    Error(app)


def register_login():
    login_manager = LoginManager()
    # login_manager.login_view = "auth.login"
    login_manager.session_protection = "basic"
    login_manager.login_message = _("Please login to access this page.")

    @login_manager.user_loader
    def user_loader(id):
        from maple.user.models import User
        user = User.query.get(int(id))
        return user

    @login_manager.request_loader
    def user_loader_from_request(request):
        from maple.user.models import User
        token = request.args.get('token')
        if token is not None:
            user = User.check_token(token)
            if user:
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


db = db
csrf = CsrfProtect()
cache = Cache()
babel = register_babel()
mail = Mail()
admin = Admin(name='HonMaple', template_mode='bootstrap3')
login_manager = register_login()
redis_data = Redis()
middleware = Middleware()
maple_app = App(json=CustomJSONEncoder)
