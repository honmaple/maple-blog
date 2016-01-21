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
from wtforms import StringField,SubmitField,PasswordField,BooleanField,\
    validators

class RegisterForm(Form):
    name = StringField('用户名', [validators.Length(min=4, max=25)])
    email = StringField('邮箱', [validators.Length(min=4, max=25)])
    passwd = PasswordField('密码', [validators.Required()])
    register = SubmitField('注册')

class LoginForm(Form):
    name = StringField('用户名:', [validators.Length(min=4, max=25)])
    passwd = PasswordField('密码:', [validators.Required()])
    # validate_code = StringField('验证码:', [validators.Length(min=4, max=6)])
    remember_me = BooleanField('remember me', default=False)
    sign_in = SubmitField('登陆')

    # def validate_name(self, field):
        # if field.data != name:
            # raise ValidationError("用户名不存在")

    # def validate_passwd(self, field):
        # if field.data != passwd:
            # raise ValidationError("密码错误")

class ForgetPasswdForm(Form):
    confirm_email = StringField('注册邮箱', [validators.Length(min=4, max=25)])
    confirm = SubmitField('确认')

class NewPasswdForm(Form):
    new_passwd = PasswordField('新密码', [validators.Required()])
    retry_new_passwd = PasswordField('重复新密码', [validators.Required()])
    confirm = SubmitField('确认')
