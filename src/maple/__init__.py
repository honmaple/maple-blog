#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-02-12 15:56:55 (CST)
# Last Update:星期二 2017-2-14 20:35:49 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Flask
from flask_maple.lazy import LazyExtension
from api.urls import api_routers
from admin.urls import admin
from flask_cors import CORS


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register(app)
    CORS(app)
    return app


def register(app):
    api_routers(app)
    register_extensions(app)


def register_extensions(app):
    extension = LazyExtension(
        module='maple.extensions.',
        extension=['middleware', 'db', 'cache', 'login_manager'])
    extension.init_app(app)
    admin.init_app(app)
