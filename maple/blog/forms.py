#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: askform.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 17:54:07
# *************************************************************************
from flask_wtf import Form
from wtforms import (SubmitField, TextAreaField, StringField, BooleanField,
                     SelectField)
from maple.forms.forms import DataRequired


class ArticleForm(Form):
    title = StringField('标题', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired()])
    category = SelectField(
        '分类',
        choices=[('linux', 'Linux'), ('python', 'Python'), ('生活随笔', '生活随笔')],
        validators=[DataRequired()])
    tags = StringField('标签', validators=[DataRequired()])
    copy = BooleanField('是否为转载', default=False)
    post = SubmitField('提交')


class SearchForm(Form):
    content = StringField('搜索', validators=[DataRequired()])
    search = SubmitField('Search')


class CommentForm(Form):
    comment = TextAreaField('评论', validators=[DataRequired()])
    post_comment = SubmitField('发表评论')


class ReplyForm(Form):
    reply = TextAreaField('回复', validators=[DataRequired()])
    post_reply = SubmitField('发表回复')
