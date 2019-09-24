#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: maple.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-01-25 11:52:26 (CST)
# Last Update: Tuesday 2019-09-24 17:53:00 (CST)
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


def init_app(app):
    Bootstrap(
        app,
        css=(
            'css/base.css', 'css/main.css', 'css/monokai.css', 'css/lib.css',
            'css/timeline.css', 'css/night.css'),
        js=('js/main.js', 'js/highlight.js', 'js/night.js'),
        auth=False)
    Captcha(app)
    Error(app)
    App(app, json=CustomJSONEncoder)
    Middleware(app)
    Logging(app)
