#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: app.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-01 20:59:29 (CST)
# Last Update:星期六 2016-11-19 22:44:21 (CST)
#          By:
# Description:
# **************************************************************************
from flask import send_from_directory
from flask_login import current_user
from flask_principal import RoleNeed, UserNeed, identity_loaded
from os import path

__all__ = ['register_app']


def register_app(app):
    @app.route('/images/<path:filename>')
    def images(filename):
        images_path = path.join(path.pardir, 'images')
        return send_from_directory(images_path, filename)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        identity.user = current_user

        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        if hasattr(current_user, 'roles'):
            identity.provides.add(RoleNeed(current_user.roles))

        if hasattr(current_user, 'is_superuser'):
            if current_user.is_superuser:
                identity.provides.add(RoleNeed('Super'))

        if hasattr(current_user, 'is_confirmed'):
            if current_user.is_confirmed:
                identity.provides.add(RoleNeed('Writer'))

        if hasattr(current_user, 'is_authenticated'):
            if not current_user.is_authenticated:
                identity.provides.add(RoleNeed('Guest'))
