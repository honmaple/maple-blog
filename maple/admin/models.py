#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: notice_db.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-01-09 20:00:36
# *************************************************************************
from maple import db, app
from sqlalchemy.event import listens_for
from flask_admin import form
import os
import os.path as op


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


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))

    def __unicode__(self):
        return self.name


@listens_for(File, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(app.static_folder, target.path))
        except OSError:
            pass


@listens_for(Image, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(app.static_folder, target.path))
        except OSError:
            pass

        try:
            os.remove(op.join(app.static_folder, form.thumbgen_filename(
                target.path)))
        except OSError:
            pass
