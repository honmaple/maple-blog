#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: models.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:42:40
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from .base import db


class MarkDown(db.Model):
    __bind_key__ = 'mkds'
    __tablename__ = 'mkds'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(128))
    datetime = db.Column(db.String(128))
    category = db.Column(db.String(128))
    tags = db.Column(db.String(128))
    summary = db.Column(db.Text)
    body = db.Column(db.Text)

    def __init__(self, title,datetime,category,tags,summary,body):
        self.title = title
        self.datetime = datetime
        self.category = category
        self.tags = tags
        self.summary = summary
        self.body = body

    def __repr__(self):
        return "<MarkDown %r>" % self.title


