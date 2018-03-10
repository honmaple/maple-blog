#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: babel.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2018-01-25 11:50:49 (CST)
# Last Update: Saturday 2018-03-11 01:33:45 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import request
from flask_babelex import Babel, Domain
import os

translations = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, 'LANG'))
domain = Domain(translations)
babel = Babel(default_domain=domain)


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
