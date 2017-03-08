#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: models.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-03-07 20:55:23 (CST)
# Last Update:星期二 2017-3-7 20:55:25 (CST)
#          By:
# Description:
# **************************************************************************
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


class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    path = db.Column(db.String(128), nullable=False, unique=True)
    url = db.Column(db.String(360), unique=True)

    def __repr__(self):
        return "<Images %r>" % self.name

    def __str__(self):
        return self.name
