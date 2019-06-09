#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-06-07 16:47:05 (CST)
# Last Update: Friday 2019-05-24 22:54:31 (CST)
#          By:
# Description:
# ********************************************************************************
from .api.encrypt import EncryptAPI


def init_app(app):
    app.add_url_rule(
        '/api/encrypt', view_func=EncryptAPI.as_view('api.encrypt'))
