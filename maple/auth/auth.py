#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: auth.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-01 21:11:24 (CST)
# Last Update:星期六 2016-11-5 20:50:38 (CST)
#          By:
# Description:
# **************************************************************************
from flask_login import current_user, login_required
from maple.extensions import mail
from maple.user.models import User
from datetime import datetime, timedelta
from functools import wraps
from flask_maple.auth import (Auth, RegisterBaseView, ConfirmBaseView,
                              ConfirmTokenBaseView)
from maple.common.response import HTTPResponse


def check_time(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        judge = datetime.now() < current_user.send_email_time + timedelta(
            seconds=360)
        if current_user.send_email_time is not None and judge:
            return HTTPResponse(HTTPResponse.USER_EMAIL_WAIT).to_response()
        return func(*args, **kwargs)

    return decorator


class RegisterView(RegisterBaseView):
    mail = mail
    user_model = User
    use_principal = True

    def register_models(self, form):
        user = self.user_model()
        user.username = form.username.data
        user.password = form.password.data
        user.email = form.email.data
        user.roles = 'Visitor'
        user.send_email_time = datetime.now()
        user.add()
        return user


class ConfirmTokenView(ConfirmTokenBaseView):
    user_model = User
    mail = mail

    def confirm_models(self, user):
        user.is_confirmed = True
        user.confirmed_time = datetime.now()
        user.roles = 'Writer'
        user.save()


class ConfirmView(ConfirmBaseView):
    decorators = [login_required, check_time]
    mail = mail

    def email_models(self):
        current_user.send_email_time = datetime.now()
        current_user.save()


def register_auth(app):
    auth = Auth(mail=mail, user_model=User, use_principal=True)
    auth.register_view = lambda: RegisterView
    auth.confirm_view = lambda: ConfirmView
    auth.confirm_token_view = lambda: ConfirmTokenView
    auth.init_app(app)
