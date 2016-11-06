#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:03:11
# *************************************************************************
from flask import Flask
from .extensions import register_maple
from .extensions import (redis_data, csrf, cache, babel, mail, db, principals,
                         login_manager)
from .filters import register_jinja2
from .logs import register_logging
from .urls import register_routes
from .app import register_app
from maple.admin.urls import admin
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
    register(app)
    return app


def register(app):
    register_extensions(app)
    register_routes(app)
    register_jinja2(app)
    register_maple(app)
    register_logging(app)
    register_app(app)


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    cache.init_app(app)
    babel.init_app(app)
    mail.init_app(app)
    principals.init_app(app)
    admin.init_app(app)
    redis_data.init_app(app)
