#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: api.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-07-20 01:02:23 (CST)
# Last Update: Tuesday 2019-09-24 19:15:38 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import Blueprint, request
from flask_babel import gettext as _
from flask_maple.response import HTTP
from flask_maple.serializer import Serializer
from maple.extension import csrf
from maple.utils import (
    MethodView,
    AuthMethodView,
    check_params,
    filter_maybe,
)

from .model import User

site = Blueprint('api', __name__, url_prefix="/api")


class UserAPI(AuthMethodView):
    def get(self):
        data = request.data
        page, number = self.pageinfo
        params = filter_maybe(data, {"username": "username__contains"})
        ins = User.query.filter_by(**params).paginate(page, number, False)
        rep = Serializer(
            ins,
            exclude=["articles", "buckets", "timelines"],
        ).data
        return HTTP.OK(data=rep, pageinfo=ins.pages)


class LoginAPI(MethodView):
    @check_params(['username', 'password'])
    def post(self):
        data = request.data
        username = data['username']
        password = data['password']
        remember = data.pop('remember', True)
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return HTTP.BAD_REQUEST(message=_('Username or Password Error'))
        user.login(remember)
        return HTTP.OK(data={"username": user.username, "token": user.token})


def before_request():
    if request.method == "OPTIONS":
        return HTTP.OK()


def init_app(app):
    site.add_url_rule('/login', view_func=LoginAPI.as_view("login"))
    site.add_url_rule('/user', view_func=UserAPI.as_view("user"))
    csrf.exempt(site)
    app.register_blueprint(site)
    app.before_request(before_request)
