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
from wtforms import TextField,SubmitField,PasswordField,validators,SelectField
from wtforms.validators import Required, Email
from wtforms.validators import DataRequired, ValidationError

class RegisterForm(Form):
    name = TextField('用户名', [validators.Length(min=4, max=25)])
    email = TextField('邮箱', [validators.Length(min=4, max=25)])
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
    passwd = PasswordField('密码', [validators.Required()])
    edit = SubmitField('修改')
    register = SubmitField('注册')
