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
from wtforms.validators import DataRequired
from flask_babelex import lazy_gettext as _


class ArticleForm(Form):
    title = StringField(_('title'), validators=[DataRequired()])
    content = TextAreaField(_('content'), validators=[DataRequired()])
    category = SelectField(
        _('category'),
        choices=[('linux', 'Linux'), ('python', 'Python'), ('生活随笔', '生活随笔')],
        validators=[DataRequired()])
    tags = StringField(_('tags'), validators=[DataRequired()])
    copy = BooleanField(_('is reprinted'), default=False)
    post = SubmitField(_('Post comment'))


class CommentForm(Form):
    comment = TextAreaField(_('Comment'), validators=[DataRequired()])
    post_comment = SubmitField(_('Post comment'))


class SearchForm(Form):
    search = StringField(_('search'), validators=[DataRequired()])
