#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: app.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-01 20:59:29 (CST)
# Last Update:星期六 2016-11-5 12:25:54 (CST)
#          By:
# Description:
# **************************************************************************
from flask import (send_from_directory, request, g)
from flask.json import JSONEncoder
from flask_login import current_user
from flask_principal import RoleNeed, UserNeed, identity_loaded

__all__ = ['register_app']


def register_app(app):
    @app.before_request
    def before_request():
        from maple.blog.forms import SearchForm
        g.search_form = SearchForm()
        g.user = current_user

    @app.route('/robots.txt')
    @app.route('/favicon.ico')
    def static_from_root():
        return send_from_directory(app.static_folder, request.path[1:])

    class CustomJSONEncoder(JSONEncoder):
        def default(self, obj):
            from speaklater import is_lazy_string
            if is_lazy_string(obj):
                try:
                    return unicode(obj)  # python 2
                except NameError:
                    return str(obj)  # python 3
            return super(CustomJSONEncoder, self).default(obj)

    app.json_encoder = CustomJSONEncoder

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
