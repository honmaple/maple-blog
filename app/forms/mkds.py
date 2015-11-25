#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: admin.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 04:44:10
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required

class MkdsForm(Form):
    title = StringField('标题',validators=[Required()])
    datetime = StringField('日期时间', validators=[Required()])
    category = StringField('分类',validators=[Required()])
    tags = StringField('标签',validators=[Required()])
    summary = TextAreaField('概要',validators=[Required()])
    body = TextAreaField('内容',validators=[Required()])
    post = SubmitField('提交')
    save = SubmitField('保存')
