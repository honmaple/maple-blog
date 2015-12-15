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
from wtforms import StringField,SubmitField,TextAreaField,\
    SelectField
from wtforms.validators import Required

class ArticleForm(Form):
    title = StringField('标题',validators=[Required()])
    content = TextAreaField('内容',validators=[Required()])
    category = SelectField('分类',
                           choices=[('linux', 'Linux'), ('python', 'Python'),
                                    ('生活随笔','生活随笔')],
                           validators=[Required()])
    tags = StringField('标签', validators=[Required()])
    post = SubmitField('提交')
