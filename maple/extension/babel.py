#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: babel.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-01-25 11:50:49 (CST)
# Last Update: Wednesday 2019-05-29 00:09:50 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from flask_babel import Babel

babel = Babel()


@babel.localeselector
def localeselector():
    if request.path.startswith('/admin'):
        return 'zh_Hans_CN'
    return request.accept_languages.best_match(['zh', 'en'])


@babel.timezoneselector
def timezoneselector():
    return 'UTC'


def init_app(app):
    babel.init_app(app)
