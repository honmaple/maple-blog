#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: login.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-01-25 11:49:01 (CST)
# Last Update: Tuesday 2018-11-06 13:52:22 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_login import LoginManager, login_user
from flask_babel import lazy_gettext as _

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(id):
    from maple.model import User
    user = User.query.get(int(id))
    return user


@login_manager.request_loader
def user_loader_from_request(request):
    from maple.model import User
    token = request.headers.get('Token')
    if not token:
        token = request.args.get('token')
    if token is not None:
        user = User.check_token(token)
        if user:
            login_user(user, True)
            return user


def init_app(app):
    # login_manager.login_view = "auth.login"
    login_manager.session_protection = "basic"
    login_manager.login_message = _("Please login to access this page.")
    login_manager.init_app(app)
