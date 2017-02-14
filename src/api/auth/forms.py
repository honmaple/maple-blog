#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: forms.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-25 15:57:27 (CST)
# Last Update:星期日 2016-12-25 15:58:19 (CST)
#          By:
# Description:
# **************************************************************************
from flask import flash, session, request
from wtforms import (StringField, PasswordField, BooleanField)
from wtforms.validators import Length, DataRequired, Email
from flask_babelex import lazy_gettext as _
from flask_maple.response import HTTPResponse
from functools import wraps

try:
    from flask_wtf import FlaskForm as Form
except ImportError:
    from flask_wtf import Form


def form_validate(form_class, success=None, error=None, f=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            form = form_class()
            if form.validate_on_submit():
                return func(*args, **kwargs)
            elif form.errors:
                if f is not None:
                    if callable(f):
                        flash(f())
                    elif f == '':
                        flash_errors(form)
                    else:
                        flash(f)
                if error is not None:
                    return error()
                return return_errors(form)
            if success is not None:
                return success()
            return HTTPResponse(HTTPResponse.NORMAL_STATUS).to_response()

        return wrapper

    return decorator


def flash_errors(form):
    for field, errors in form.errors.items():
        flash(u"%s %s" % (getattr(form, field).label.text, errors[0]))
        break


def return_errors(form):
    for field, errors in form.errors.items():
        data = (u"%s %s" % (getattr(form, field).label.text, errors[0]))
        break
    return HTTPResponse(
        HTTPResponse.FORM_VALIDATE_ERROR, description=data).to_response()


class BaseForm(Form):
    username = StringField(
        _('Username:'), [DataRequired(), Length(
            min=4, max=20)])
    password = PasswordField(
        _('Password:'), [DataRequired(), Length(
            min=4, max=20)])
    captcha = StringField(
        _('Captcha:'), [DataRequired(), Length(
            min=4, max=4)])

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        captcha = session['captcha']
        captcha_data = self.captcha.data
        if captcha_data.lower() != captcha.lower():
            self.captcha.errors.append(_('The captcha is error'))
            return False

        return True


class RegisterForm(BaseForm):
    email = StringField(_('Email:'), [DataRequired(), Email()])


class LoginForm(BaseForm):
    remember = BooleanField(_('Remember me'), default=False)


class ForgetForm(Form):
    email = StringField(_('Register Email:'), [DataRequired(), Email()])

    captcha = StringField(
        _('Captcha:'), [DataRequired(), Length(
            min=4, max=4)])

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        captcha = session['captcha']
        captcha_data = self.captcha.data
        if captcha_data.lower() != captcha.lower():
            self.captcha.errors.append(_('The captcha is error'))
            return False

        return True
