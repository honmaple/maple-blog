#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: administrator.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 21:58:14
# *************************************************************************
from flask.ext.wtf import Form
from wtforms import PasswordField, StringField, TextAreaField
from maple.forms.forms import DataRequired, Length, EqualTo


class EditUserInforForm(Form):
    introduce = TextAreaField('个人介绍', [DataRequired()])
    school = StringField('学校/公司', [DataRequired()])


class EditPasswdForm(Form):
    passwd = PasswordField('密码', [DataRequired()])
    new_passwd = PasswordField('新密码',
                               [DataRequired(), Length(min=4,
                                                       max=20),
                                EqualTo('retry_new_passwd')])
    retry_new_passwd = PasswordField('重复新密码', [DataRequired()])
