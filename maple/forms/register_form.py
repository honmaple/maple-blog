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
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Length,Required,EqualTo,Email
from wtforms.widgets import SubmitInput

class RegisterForm(Form):
    name = StringField('用户名:',
                       [Required(message='用户名不能为空'),
                        Length(min=4,
                               max=20,
                               message='用户名长度在4到20个字符之间')])
    email = StringField('邮箱',
                        [Required(message='邮箱不能为空'),
                         Email(message='错误的邮箱地址')])
    passwd = PasswordField('密码',
                           [Required(message='密码不能为空'),
                            Length(min=4,
                                   max=20,
                                   message='密码长度在4到20个字符之间')])
    register = SubmitField('注册')
    hello = SubmitInput('hello')

class LoginForm(Form):
    name = StringField('用户名:',
                       [Required(message='用户名不能为空'),
                        Length(min=4,
                               max=20,
                               message='用户名长度在4到20个字符之间')])
    passwd = PasswordField('密码:',
                           [Required(message='密码不能为空'),
                            Length(min=4,
                                   max=20,
                                   message='密码长度在4到20个字符之间')])
    remember_me = BooleanField('remember me', default=False)
    sign_in = SubmitField('登陆')

class ForgetPasswdForm(Form):
    confirm_email = StringField('注册邮箱',
                                [Required(message='邮箱不能为空'),
                                 Email(message='错误的邮箱地址')])
    confirm = SubmitField('确认')

class NewPasswdForm(Form):
    new_passwd = PasswordField('新密码',
                               [Required(message=u'密码不能为空'),
                                Length(min=4,
                                       max=20,
                                       message='密码长度在4到20个字符之间'),
                                EqualTo('retry_new_passwd',
                                        message=u'两次密码不一致')])
    retry_new_passwd = PasswordField('重复新密码',
                                     [Required(message=u'密码不能为空')])
    confirm = SubmitField('确认')


