#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 22:50:14 (CST)
# Last Update: Friday 2019-05-24 23:32:44 (CST)
#          By:
# Description:
# ********************************************************************************
from .timeline import TimeLineAPI


def init_app(app):
    app.add_url_rule(
        '/api/timeline', view_func=TimeLineAPI.as_view('api.timeline'))
