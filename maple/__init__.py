#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:03:11
# *************************************************************************
from flask import (Flask, send_from_directory, request, g)
from flask_mail import Mail
from flask_principal import Principal
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from .extensions import (register_maple, register_form, register_babel,
                         register_login)
from .extensions import register_redis, register_cache
from .filters import register_jinja2
from .logs import register_logging
import os


def create_app(config=None):
    templates = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
    app = Flask(__name__, template_folder=templates, static_folder=static)
    if config is None:
        app.config.from_object('config.config')
    else:
        app.config.from_object(config)
    return app


def register(app):
    register_babel(app)
    register_form(app)
    register_jinja2(app)
    register_login(app)
    register_maple(app)
    register_routes(app)
    register_logging(app)


def register_routes(app):
    from .urls import register_urls
    register_urls(app)


app = create_app()
db = SQLAlchemy(app)
mail = Mail(app)
principals = Principal(app)
redis_data = register_redis(app)
cache = register_cache(app)
register(app)


@app.before_request
def before_request():
    from maple.blog.forms import SearchForm
    g.search_form = SearchForm()
    g.user = current_user


@app.route('/robots.txt')
@app.route('/favicon.ico')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
