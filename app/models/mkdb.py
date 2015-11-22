#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# from .base import db
from .base import db

class MarkDown(db.Model):
    __bind_key__ = 'mkds'
    __tablename__ = 'mkd'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)

    def __init__(self, title,body,body_html):
        self.title = title
        self.body = body
        self.body_html = body_html

    def __repr__(self):
        return "<MarkDown %r>" % self.title


