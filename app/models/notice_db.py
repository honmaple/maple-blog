#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: notice_db.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-01-09 20:00:36
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from .base import db

# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/articledb'
# db = SQLAlchemy(app)
class Notices(db.Model):
    __bind_key__ = 'blog'
    __tablename__ = 'notices'
    id = db.Column(db.Integer,primary_key=True)
    notice = db.Column(db.Text,nullable=False)
    publish = db.Column(db.DateTime, nullable=False)

    def __init__(self,notice):
        self.notice = notice

    def __repr__(self):
        return "<Notices %r>" % self.title

