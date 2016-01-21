#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: administrator.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 21:58:14
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField,validators,\
    SelectField,TextAreaField
from wtforms.validators import Required


class EditUserInforForm(Form):
    passwd = PasswordField('密码', [validators.Required()])
    new_passwd = PasswordField('新密码', [validators.Length(min=4, max=25)])
    retry_new_passwd = PasswordField('重复新密码', 
                                     [validators.Length(min=4, max=25)])
    introduce = TextAreaField('个人介绍', [validators.Required()])
    school = StringField('学校/公司', [validators.Required()])
    edit = SubmitField('修改')

class EditRegisterForm(Form):
    name = StringField('用户名', [validators.Length(min=4, max=25)])
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

