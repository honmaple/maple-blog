#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: askform.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 17:54:07
# *************************************************************************
from flask_wtf import FlaskForm as Form
from wtforms import (SubmitField, TextAreaField, StringField)
from wtforms.validators import DataRequired
from flask_babelex import lazy_gettext as _


class CommentForm(Form):
    content = TextAreaField(_('Comment'), validators=[DataRequired()])
    submit = SubmitField(_('Post comment'))


class SearchForm(Form):
    search = StringField(_('search'), validators=[DataRequired()])
