# !/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: forms.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-10-29 07:09:54
# *************************************************************************
from flask.ext.wtf import Form
from wtforms import (StringField, PasswordField, BooleanField)
from wtforms.validators import Length, DataRequired, Email
from flask_babel import lazy_gettext as _
from maple.user.models import User


class BaseForm(Form):
    name = StringField(_('Username:'), [DataRequired(), Length(min=4, max=20)])
    passwd = PasswordField(
        _('Password:'), [DataRequired(), Length(min=4, max=20)])
    code = StringField(_('Captcha:'), [DataRequired(), Length(min=4, max=4)])


class RegisterForm(BaseForm):
    email = StringField(_('Email:'), [DataRequired(), Email()])


class LoginForm(BaseForm):
    remember = BooleanField(_('Remember me'), default=False)

    def __init__(self, *args, **kwargs):
        BaseForm.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = BaseForm.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(name=self.name.data).first()
        print(user)
        if user is None:
            self.name.errors.append('Unknown username')
            return False

        a = User()
        if not user.check_password(self.passwd.data):
            self.passwd.errors.append('Invalid password')
            return False

        self.user = user
        return True


class ForgetPasswdForm(Form):
    confirm_email = StringField(
        _('Register Email:'), [DataRequired(), Email()])
    code = StringField(_('Captcha:'), [DataRequired(), Length(min=4, max=4)])
