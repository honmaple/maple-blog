#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
# Copyright © 2015 JiangLin. All rights reserved.
# File Name: __init__.py
# Author:JiangLin
# Mail:mail@honmaple.com
# Created Time: 2015-11-18 08:03:11
# *************************************************************************
from flask import Flask
from maple import extension, router, jinja, admin, alias, api
from werkzeug import import_string
import os


def create_app(config):
    templates = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'templates'))
    static = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, 'static'))
    app = Flask(__name__, template_folder=templates, static_folder=static)
    app.config.from_object(config)
    app.url_map.redirect_defaults = False

    extension.init_app(app)
    jinja.init_app(app)
    admin.init_app(app)
    router.init_app(app)
    api.init_app(app)
    alias.init_app(app)

    apps = ["maple.blog", "maple.storage", "maple.tool"]
    [import_string(i).init_app(app) for i in apps]

    return app
