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
from wtforms import StringField,SubmitField,PasswordField,validators
from wtforms.validators import Required, Email

class LoginForm(Form):
    name = StringField('用户名:', [validators.Length(min=4, max=25)])
    passwd = PasswordField('密码:', [
        validators.Required()
    ])
    # validate_code = StringField('验证码:', [validators.Length(min=4, max=6)])
    sign_in = SubmitField('登陆')

    # def validate_name(self, field):
        # if field.data != name:
            # raise ValidationError("用户名不存在")

    # def validate_passwd(self, field):
        # if field.data != passwd:
            # raise ValidationError("密码错误")
