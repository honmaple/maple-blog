#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: maple.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2018-01-25 11:52:26 (CST)
# Last Update: Sunday 2018-03-11 17:32:54 (CST)
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
    css=('css/honmaple.css', 'css/monokai.css', 'css/lib.css'),
    js=('js/highlight.js', 'js/rain.js', 'js/org.js'),
    use_auth=False)


def init_app(app):
    bootstrap.init_app(app)
    Captcha(app)
    Error(app)
    App(app, json=CustomJSONEncoder)
    Middleware(app)
    Logging(app)
