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

class Articledb(db.Model):
    __bind_key__ = 'articles'
    __tablename__ = 'articles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    title = db.Column(db.String,nullable=False)
    describ = db.Column(db.Text)
    answer = db.Column(db.Text)
    publish = db.Column(db.DateTime, nullable=False)

    def __init__(self, name,title,describ,answer,
                 publish = datetime.datetime.now()):
        self.name = name
        self.title = title
        self.describ = describ
        self.answer = answer
        self.publish = publish

    def __repr__(self):
        return "<Articledb %r>" % self.title

# from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qaz123@localhost/article'
# db = SQLAlchemy(app)


# import datetime

# class Articledb(db.Model):
    # __tablename__ = 'articles'
    # id = db.Column(db.Integer,primary_key=True)
    # name = db.Column(db.String, nullable=False)
    # title = db.Column(db.String,nullable=False)
    # describ = db.Column(db.Text)
    # answer = db.Column(db.Text)
    # publish = db.Column(db.DateTime, nullable=False)

    # def __init__(self, name,title,describ,answer,
                 # publish = datetime.datetime.now()):
        # self.name = name
        # self.title = title
        # self.describ = describ
        # self.answer = answer
        # self.publish = publish

    # def __repr__(self):
        # return "<Articledb %r>" % self.title
