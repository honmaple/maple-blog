#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:mail@honmaple.com
#   Created Time: 2015-11-18 08:03:11
# *************************************************************************
from flask import Flask
from maple import extension, admin, blueprint, jinja, api
from maple import app as ap
import os


def create_app(config):
    templates = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
    app = Flask(__name__, template_folder=templates, static_folder=static)
    app.config.from_object(config)

    extension.init_app(app)
    jinja.init_app(app)
    admin.init_app(app)
    ap.init_app(app)
    blueprint.init_app(app)
    api.init_app(app)

    return app
