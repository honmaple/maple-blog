#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: router.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-24 22:46:38 (CST)
# Last Update: Wednesday 2019-09-11 12:16:35 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import redirect, request
from flask_babel import gettext as _
from flask_maple.response import HTTP
from maple.model import User
from maple.utils import MethodView, check_params


class IndexView(MethodView):
    def get(self):
        return HTTP.HTML("index/index.html")


class AboutView(MethodView):
    def get(self):
        return HTTP.HTML("index/about.html")


class FriendView(MethodView):
    def get(self):
        return HTTP.HTML("index/friends.html")


class ContactView(MethodView):
    def get(self):
        return HTTP.HTML("index/contact.html")


class LoginView(MethodView):
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
        return HTTP.OK()


class LogoutView(MethodView):
    cache_time = 0

    def get(self):
        user = request.user
        user.logout()
        return redirect(request.args.get('next') or '/')


def init_app(app):
    index_view = IndexView.as_view('index')
    about_view = AboutView.as_view('about')
    friend_view = FriendView.as_view('friend')
    contact_view = ContactView.as_view('contact')
    app.add_url_rule('/', view_func=index_view)
    app.add_url_rule('/index', view_func=index_view)
    app.add_url_rule('/about', view_func=about_view)
    app.add_url_rule('/friends', view_func=friend_view)
    app.add_url_rule('/contact', view_func=contact_view)
    app.add_url_rule('/login', view_func=LoginView.as_view("login"))
    app.add_url_rule('/logout', view_func=LogoutView.as_view("logout"))
