#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: askform.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 17:54:07
# *************************************************************************
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired


class QuestionForm(Form):
    title = StringField('问题:', validators=[DataRequired()])
    describ = TextAreaField('描述', validators=[DataRequired()])
    answer = TextAreaField('回答:', validators=[DataRequired()])
    private = BooleanField('保存为私人日记', default=False)
    post = SubmitField('提交')
