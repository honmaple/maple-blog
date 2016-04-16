#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: administrator.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 21:58:14
# *************************************************************************
from flask_wtf import Form
from wtforms import (StringField, SubmitField, PasswordField, SelectField,
                     TextAreaField)
from wtforms.validators import DataRequired, Length, EqualTo


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


class EditRegisterForm(Form):
    name = StringField('用户名', [Length(min=4, max=25)])
    is_superuser = SelectField('是否授予超级管理员权限',
                               choices=[('True', 'True'), ('False', 'False')],
                               validators=[DataRequired()])
    roles = SelectField(
        '用户组',
        choices=[('super', 'Super'), ('admin', 'Admin'), ('writer', 'Writer'),
                 ('editor', 'Editor'), ('visitor', 'Visitor')],
        validators=[DataRequired()])
    is_confirmed = SelectField('修改用户验证状态',
                               choices=[('True', 'True'), ('False', 'False')],
                               validators=[DataRequired()])
    edit = SubmitField('修改')


class NoticesForm(Form):
    notice = TextAreaField('公告内容', [DataRequired()])
    confirm = SubmitField('发布公告')
