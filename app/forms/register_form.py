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
from wtforms import TextField,SubmitField,PasswordField,validators
from wtforms.validators import Required, Email
from wtforms.validators import DataRequired, ValidationError

class RegisterForm(Form):
    name = TextField('用户名', [validators.Length(min=4, max=25)])
    email = TextField('邮箱', [validators.Length(min=4, max=25)])
    passwd = PasswordField('密码', [
        validators.Required()
    ])
    register = SubmitField('注册')
