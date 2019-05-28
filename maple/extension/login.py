#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: login.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-01-25 11:49:01 (CST)
# Last Update: Friday 2019-05-24 23:01:01 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_login import LoginManager, login_user
from flask_babel import lazy_gettext as _
from flask_maple.response import HTTP

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(id):
    from maple.model import User
    return User.query.get(int(id))


@login_manager.request_loader
def request_loader(request):
    from maple.model import User
    token = request.headers.get('Token', request.args.get('token'))
    user = None
    if token:
        user = User.check_token(token)
    if not user:
        return
    login_user(user, True)
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return HTTP.UNAUTHORIZED()


def init_app(app):
    # login_manager.login_view = "auth.login"
    login_manager.session_protection = "basic"
    login_manager.login_message = _("Please login to access this page.")
    login_manager.init_app(app)
