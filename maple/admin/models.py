#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: notice_db.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-01-09 20:00:36
# *************************************************************************
from maple import db


class Notices(db.Model):
    __tablename__ = 'notices'
    id = db.Column(db.Integer, primary_key=True)
    notice = db.Column(db.Text, nullable=False)
    publish = db.Column(db.DateTime, nullable=False)

    __mapper_args__ = {"order_by": publish.desc()}

    def __init__(self, notice):
        self.notice = notice

    def __repr__(self):
        return "<Notices %r>" % self.title
