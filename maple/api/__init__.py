#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-03-11 20:51:31 (CST)
# Last Update: Tuesday 2018-11-06 13:52:22 (CST)
#          By:
# Description:
# ********************************************************************************
from maple.api.timeline import TimeLineAPI
from maple.api.encrypt import EncryptAPI


def init_app(app):
    app.add_url_rule(
        '/api/timeline', view_func=TimeLineAPI.as_view('api.timeline'))
    app.add_url_rule(
        '/api/encrypt', view_func=EncryptAPI.as_view('api.encrypt'))
