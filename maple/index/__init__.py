# !/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-11 16:22:33 (CST)
# Last Update: 星期一 2018-02-05 17:14:43 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import (IView, IndexView, AboutView, RainView, FriendView)

site = Blueprint('index', __name__)

index_view = IndexView.as_view('index')
rain_view = RainView.as_view('rain')
about_view = AboutView.as_view('about')
friend_view = FriendView.as_view('friend')
site.add_url_rule('/', view_func=IView.as_view('i'))
site.add_url_rule('/index', view_func=index_view)
site.add_url_rule('/rain', view_func=rain_view)
site.add_url_rule('/about', view_func=about_view)
site.add_url_rule('/friends', view_func=friend_view)


def init_app(app):
    app.register_blueprint(site)
