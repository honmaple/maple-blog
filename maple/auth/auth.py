#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: auth.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-01 21:11:24 (CST)
# Last Update:星期二 2016-11-1 21:11:26 (CST)
#          By:
# Description:
# **************************************************************************
from flask import jsonify
from flask_maple import Auth
from flask_login import current_user, login_required
from flask_babelex import gettext as _
from maple import app, db, mail
from maple.user.models import User
from datetime import datetime, timedelta
from functools import wraps


def check_time(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if current_user.send_email_time is None:
            pass
        else:
            if datetime.now() < current_user.send_email_time + timedelta(
                    seconds=360):
                return jsonify(judge=False,
                               error="Your confirm link have not out of time,"
                               + "Please confirm your email in time")
        return func(*args, **kwargs)

    return decorator


class Login(Auth):
    def register_models(self, form):
        user = self.User()
        user.username = form.username.data
        user.password = user.set_password(form.password.data)
        user.email = form.email.data
        user.roles = 'Visitor'
        user.send_email_time = datetime.now()
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def confirm_models(self, user):
        user.is_confirmed = True
        user.confirmed_time = datetime.now()
        user.roles = 'Writer'
        self.db.session.commit()

    @login_required
    @check_time
    def confirm_email(self):
        if current_user.is_confirmed:
            return jsonify(
                judge=False,
                error=_('Your account has been confirmed,don\'t need again'))
        else:
            self.register_email(current_user.email)
            self.email_models()
            return jsonify(
                judge=True,
                error=_('An email has been sent to your.Please receive'))


Login(app, db=db, mail=mail, user_model=User, use_principal=True)
