#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: forms.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-10-29 07:09:54
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask_wtf import Form
from wtforms import TextField,SubmitField,PasswordField,validators
from wtforms.validators import Required, Email
from wtforms.validators import DataRequired, ValidationError

class LoginForm(Form):
    name = TextField('Username', [validators.Length(min=4, max=25)])
    passwd = PasswordField('Password', [
        validators.Required("please")
    ])
    sign_in = SubmitField('Sign in')

    # def validate_name(self, field):
        # if field.data != name:
            # raise ValidationError("用户名不存在")

    # def validate_passwd(self, field):
        # if field.data != passwd:
            # raise ValidationError("密码错误")
