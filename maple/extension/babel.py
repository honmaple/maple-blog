#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: babel.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-01-25 11:50:49 (CST)
# Last Update: Friday 2018-11-16 16:52:55 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from flask_babel import Babel

babel = Babel()


@babel.localeselector
def locale():
    if request.path.startswith('/admin'):
        return 'zh_Hans_CN'
    return request.accept_languages.best_match(['zh', 'en'])


@babel.timezoneselector
def timezone():
    return 'UTC'


def init_app(app):
    babel.init_app(app)
