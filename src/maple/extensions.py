#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: extensions.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-02-12 16:17:43 (CST)
# Last Update:星期二 2017-2-14 20:35:26 (CST)
#          By:
# Description:
# **************************************************************************
from flask import abort
from flask_admin import Admin
from flask_maple.models import db
from flask_maple.middleware import Middleware
from flask_cache import Cache
from flask_login import LoginManager
from common.helper import config


def register_login():
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "basic"
    login_manager.login_message = "Please login to access this page."

    @login_manager.user_loader
    def user_loader(id):
        from api.user.models import User
        user = User.query.get(int(id))
        return user

    @login_manager.request_loader
    def user_loader_from_request(request):
        from api.user.models import User
        token = request.headers.get(config['LOGIN_TOKEN_HEADER'], None)
        if not token:
            token = request.args.get(config['LOGIN_TOKEN'], None)
        if token:
            user = User.check_user_token(token)
            if user and user.user_status == User.USER_STATUS_ACTIVED:
                return user

    @login_manager.unauthorized_handler
    def unauthorized():
        abort(403)

    return login_manager


db = db
middleware = Middleware()
cache = Cache()
login_manager = register_login()
admin = Admin(name='HonMaple', template_mode='bootstrap3')
