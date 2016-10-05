#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: extensions.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-02 12:35:57 (CST)
# Last Update:星期三 2016-10-5 15:16:8 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request
from flask.json import JSONEncoder
from flask_maple import Bootstrap, Captcha, Error
from flask_wtf.csrf import CsrfProtect
from flask_login import LoginManager
from redis import StrictRedis
from flask_cache import Cache
from flask_babelex import Babel, Domain
from flask_babelex import lazy_gettext as _
import os


def register_form(app):
    csrf = CsrfProtect()
    csrf.init_app(app)


def register_maple(app):
    maple = Bootstrap(css=('style/honmaple.css', 'style/monokai.css'),
                      use_auth=True)
    maple.init_app(app)
    Captcha(app)
    Error(app)


def register_redis(app):
    config = app.config
    redis_data = StrictRedis(db=config['CACHE_REDIS_DB'],
                             password=config['CACHE_REDIS_PASSWORD'])
    return redis_data


def register_cache(app):
    cache = Cache()
    cache.init_app(app)
    return cache


def register_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message = _("Please login to access this page.")

    from maple.user.models import User

    @login_manager.user_loader
    def user_loader(id):
        user = User.query.get(int(id))
        return user


def register_babel(app):
    translations = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir, 'translations'))
    domain = Domain(translations)
    babel = Babel(default_domain=domain)
    babel.init_app(app)

    class CustomJSONEncoder(JSONEncoder):
        """This class adds support for lazy translation texts to Flask's
        JSON encoder. This is necessary when flashing translated texts."""

        def default(self, obj):
            from speaklater import is_lazy_string
            if is_lazy_string(obj):
                try:
                    return unicode(obj)  # python 2
                except NameError:
                    return str(obj)  # python 3
            return super(CustomJSONEncoder, self).default(obj)

    app.json_encoder = CustomJSONEncoder

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(['zh', 'en'])

    @babel.timezoneselector
    def get_timezone():
        return 'UTC'
