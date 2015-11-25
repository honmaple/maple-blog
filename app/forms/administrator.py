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
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required, Email

class AdminForm(Form):
    name = StringField('User:',validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    passwd=PasswordField('Password:',validators=[Required()])
    login_in = SubmitField('Sign in')
