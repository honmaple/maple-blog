#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: askform.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 17:54:07
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import SubmitField,TextAreaField
from wtforms.validators import Required

class CommentForm(Form):
    comment = TextAreaField('评论', validators=[Required()])
    post_comment = SubmitField('发表评论')

class ReplyForm(Form):
    reply = TextAreaField('回复', validators=[Required()])
    post_reply = SubmitField('发表回复')
