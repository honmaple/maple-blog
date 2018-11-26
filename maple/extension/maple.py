#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: maple.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-01-25 11:52:26 (CST)
# Last Update: Wednesday 2018-11-21 11:00:34 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_maple.bootstrap import Bootstrap
from flask_maple.captcha import Captcha
from flask_maple.error import Error
from flask_maple.app import App
from flask_maple.json import CustomJSONEncoder
from flask_maple.middleware import Middleware
from flask_maple.log import Logging

bootstrap = Bootstrap(
    css=('css/main.css', 'css/monokai.css', 'css/lib.css', 'css/timeline.css'),
    js=('js/main.js', 'js/highlight.js', 'js/rain.js', 'js/org.js'),
    auth=False)


def init_app(app):
    bootstrap.init_app(app)
    Captcha(app)
    Error(app)
    App(app, json=CustomJSONEncoder)
    Middleware(app)
    Logging(app)
