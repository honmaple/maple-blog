#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2018-03-11 20:51:31 (CST)
# Last Update: Sunday 2018-03-11 20:58:16 (CST)
#          By:
# Description:
# ********************************************************************************
from maple.api.timeline import TimeLineAPI


def init_app(app):
    app.add_url_rule(
        '/api/timeline', view_func=TimeLineAPI.as_view('api.timeline'))
