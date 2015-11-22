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
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required, Email

class UserForm(Form):
    name = StringField('User:',validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    passwd=PasswordField('Password:',validators=[Required()])
    sign_in = SubmitField('Sign in')
    sign_up = SubmitField('Sign up')
