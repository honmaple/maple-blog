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
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class MkdForm(Form):
    title = StringField('Title:',validators=[Required()])
    body = StringField('Body', validators=[Required()])
    body_html = StringField('Body_html:',validators=[Required()])
    post = SubmitField('提交')
