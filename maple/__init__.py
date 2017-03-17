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
from flask_maple.lazy import LazyExtension
from .extensions import register_maple
from .filters import register_jinja2
from .logs import register_logging
from .urls import register_routes
from .app import register_app
from maple.admin.urls import admin
import os


def create_app(config):
    templates = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
    app = Flask(__name__, template_folder=templates, static_folder=static)
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

    # from flask import render_template

    # @app.route('/admin')
    # def aaaa():
    #     return render_template('admin/base.html')


def register_extensions(app):
    extension = LazyExtension(
        module='maple.extensions.',
        extension=['db', 'login_manager', 'csrf', 'cache', 'babel',
                   'principals', 'redis_data', 'maple_app', 'middleware',
                   'mail'])
    extension.init_app(app)
    admin.index_view.url = app.config['ADMIN_URL']
    admin.init_app(app)
