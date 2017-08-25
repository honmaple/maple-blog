#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: lin.jiang@upai.com
# Created: 2017-08-24 14:30:21 (CST)
# Last Update:星期四 2017-8-24 14:30:49 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import QueListView, QuePrivateView, QueView

site = Blueprint('question', __name__)

site.add_url_rule('/', view_func=QueListView.as_view('quelist'))
site.add_url_rule('/private', view_func=QuePrivateView.as_view('privatelist'))
site.add_url_rule('/<int:queId>', view_func=QueView.as_view('que'))


def init_app(app):
    app.register_blueprint(site, url_prefix='/question')
