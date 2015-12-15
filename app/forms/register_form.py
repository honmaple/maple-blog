#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: forms.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-10-29 07:09:54
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField,validators,SelectField
from wtforms.validators import Required

class RegisterForm(Form):
    name = StringField('用户名', [validators.Length(min=4, max=25)])
    email = StringField('邮箱', [validators.Length(min=4, max=25)])
    passwd = PasswordField('密码', [validators.Required()])
    new_passwd = PasswordField('新密码', [validators.Required()])
    retry_new_passwd = PasswordField('重复新密码', [validators.Required()])
    is_superuser = SelectField('是否授予超级管理员权限',
                           choices=[('True','True'), ('False', 'False')],
                           validators=[Required()])
    roles = SelectField('用户组',
                           choices=[('super','Super'),('admin', 'Admin'), 
                                    ('writer', 'Writer'),('editor','Editor'),
                                    ('visitor','Visitor')],
                           validators=[Required()])
    is_confirmed = SelectField('修改用户验证状态',
                               choices=[('True','True'), ('False', 'False')],
                               validators=[Required()])
    edit = SubmitField('修改')
    register = SubmitField('注册')

    confirm_email = StringField('注册邮箱', [validators.Length(min=4, max=25)])
    confirm = SubmitField('确认')

