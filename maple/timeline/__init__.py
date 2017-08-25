#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-13 14:42:10 (CST)
# Last Update:星期四 2017-8-24 14:29:0 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint

from .views import TimeLineListView

site = Blueprint('timeline', __name__)
timelinelist_view = TimeLineListView.as_view('timelinelist')
site.add_url_rule('', view_func=timelinelist_view)


def init_app(app):
    app.register_blueprint(site, url_prefix='/timeline')
