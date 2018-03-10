#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: app.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2018-03-11 00:56:32 (CST)
# Last Update: Saturday 2018-03-11 00:57:32 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import redirect, request
from flask_login import current_user, login_required, login_user, logout_user


def init_app(app):
    @app.route('/login')
    @login_required
    def login():
        user = current_user._get_current_object()
        login_user(user, remember=True)
        return 'hello world'

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(request.args.get('next') or '/')
