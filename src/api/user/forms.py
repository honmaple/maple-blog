#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: administrator.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 21:58:14
# *************************************************************************
from flask_wtf import FlaskForm as Form
from wtforms import PasswordField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class InforForm(Form):
    introduce = TextAreaField('个人介绍', [DataRequired()])
    school = StringField('学校/公司', [DataRequired()])


class PasswordForm(Form):
    passwd = PasswordField('密码', [DataRequired()])
    new_passwd = PasswordField(
        '新密码', [DataRequired(), Length(
            min=4, max=20), EqualTo(
                'retry_new_passwd', message='密码输入要一致')])
    retry_new_passwd = PasswordField('重复新密码', [DataRequired()])
