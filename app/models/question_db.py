#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: articledb.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-29 02:07:53
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from .base import db
import datetime

class Questions(db.Model):
    __bind_key__ = 'blog'
    __tablename__ = 'questions'
    id = db.Column(db.Integer,primary_key=True)
    user = db.Column(db.String, nullable=False)
    title = db.Column(db.String,nullable=False)
    describ = db.Column(db.Text)
    answer = db.Column(db.Text)
    publish = db.Column(db.DateTime, nullable=False)

    def __init__(self,
                 user,title,
                 describ,answer,
                 publish = datetime.datetime.now().strftime('%F %X')):
        self.user = user
        self.title = title
        self.describ = describ
        self.answer = answer
        self.publish = publish
    def __repr__(self):
        return "<Questions %r>" % self.title

# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/articledb'
# db = SQLAlchemy(app)


# import datetime

# class Questions(db.Model):
    # __tablename__ = 'questions'
    # id = db.Column(db.Integer,primary_key=True)
    # user = db.Column(db.String, nullable=False)
    # title = db.Column(db.String,nullable=False)
    # describ = db.Column(db.Text)
    # answer = db.Column(db.Text)
    # publish = db.Column(db.DateTime, nullable=False)

    # def __init__(self,
                 # user,questiion_title,
                 # describ,answer,
                 # publish = datetime.datetime.now().strftime('%F %X')):
        # self.user = user
        # self.questiion_title = questiion_title
        # self.describ = describ
        # self.answer = answer
        # self.publish = publish
    # def __repr__(self):
        # return "<Questions %r>" % self.title
