#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: app.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-03-11 00:56:32 (CST)
# Last Update: Wednesday 2018-11-21 14:02:17 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import redirect, request
from flask_login import current_user, login_required, login_user, logout_user
from flask_maple.response import HTTP


def init_app(app):
    @app.route('/login')
    @login_required
    def login():
        user = current_user._get_current_object()
        login_user(user, remember=True)
        return HTTP.OK()

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(request.args.get('next') or '/')
