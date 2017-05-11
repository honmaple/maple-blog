#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: app.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-01 20:59:29 (CST)
# Last Update:星期四 2017-5-11 16:20:45 (CST)
#          By:
# Description:
# **************************************************************************
from flask import send_from_directory, redirect, request
from flask_login import current_user, login_required, login_user, logout_user
from os import path

__all__ = ['register_app']


def register_app(app):
    @app.route('/images/<path:filename>')
    def images(filename):
        images_path = path.join(app.static_folder, 'images')
        return send_from_directory(images_path, filename)

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
