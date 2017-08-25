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
from maple import apps, filters, logs, extensions
from importlib import import_module
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
    extensions.init_app(app)
    apps.init_app(app)
    filters.init_app(app)
    logs.init_app(app)

    blueprints = app.config.get('MAPLE_BLUEPRINT', [])
    for blueprint in blueprints:
        blueprint = import_module(blueprint)
        blueprint.init_app(app)
