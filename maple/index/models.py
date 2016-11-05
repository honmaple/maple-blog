#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: notice_db.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-01-09 20:00:36
# *************************************************************************
from maple.extensions import db
from datetime import datetime


class Notice(db.Model):
    __tablename__ = 'notices'
    id = db.Column(db.Integer, primary_key=True)
    notice = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)

    __mapper_args__ = {"order_by": created_at.desc()}

    def __repr__(self):
        return "<Notice %r>" % self.id

    def __str__(self):
        return self.notice
