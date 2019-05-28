#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: db.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:05 (CST)
# Last Update: Friday 2019-06-07 14:44:34 (CST)
#          By:
# Description:
# ********************************************************************************
import os

from flask_maple.models import ModelTimeMixin, ModelUserMixin
from sqlalchemy import event
from sqlalchemy.orm.attributes import get_history

from maple.extension import db
from . import config


class Bucket(ModelUserMixin, db.Model):
    __tablename__ = 'bucket'

    name = db.Column(db.String(108), nullable=False, unique=True)
    description = db.Column(db.String(1024), default='default')

    @property
    def images(self):
        return self.files.filter_by(file_type=File.FILE_IMAGE)

    @property
    def abspath(self):
        return os.path.join(config.UPLOAD_FOLDER, self.name)

    def __repr__(self):
        return '<Bucket %r>' % self.name

    def __str__(self):
        return self.name


class File(ModelTimeMixin, db.Model):
    __tablename__ = 'file'

    FILE_TYPE = ("IMAGE", "CSS", "JS")
    FILE_IMAGE = "IMAGE"

    name = db.Column(db.String(108), nullable=False)
    path = db.Column(db.String(512), nullable=False, default="/")
    file_type = db.Column(db.String(108), nullable=False)
    hash = db.Column(db.String(1024), nullable=False)

    bucket_id = db.Column(
        db.Integer,
        db.ForeignKey('bucket.id', ondelete="CASCADE"),
        nullable=False)
    bucket = db.relationship(
        Bucket,
        backref=db.backref(
            'files', cascade='all,delete-orphan', lazy='dynamic'),
        uselist=False,
        lazy='joined')

    @property
    def abspath(self):
        return os.path.join(
            config.UPLOAD_FOLDER,
            self.bucket.name,
            self.path.lstrip("/"),
            self.name,
        )

    @property
    def relpath(self):
        return os.path.join(
            self.bucket.name,
            self.path.lstrip("/"),
            self.name,
        )

    def __repr__(self):
        return '<File %r>' % self.name

    def __str__(self):
        return self.name


@event.listens_for(Bucket, 'after_update')
def bucket_update_listen(mapper, connection, target):
    oldname = target.name
    newname = target.name
    history = get_history(target, "name")
    if history.added and history.deleted:
        oldname = history.deleted[0]
        newname = history.added[0]

    oldpath = os.path.join(
        config.UPLOAD_FOLDER,
        oldname,
    )
    newpath = os.path.join(
        config.UPLOAD_FOLDER,
        newname,
    )
    if oldpath != newpath and os.path.exists(oldpath):
        os.rename(oldpath, newpath)


@event.listens_for(Bucket, 'after_delete')
def bucket_delete_listen(mapper, connection, target):
    filepath = target.abspath
    if os.path.exists(filepath) and not os.listdir(filepath):
        os.rmdir(filepath)


@event.listens_for(File, 'after_update')
def file_update_listen(mapper, connection, target):
    change = {
        "name": (target.name, target.name),
        "path": (target.path, target.path),
        "bucket": (target.bucket, target.bucket)
    }
    history = get_history(target, "bucket")
    if history.added and history.deleted:
        change["bucket"] = (history.deleted[0], history.added[0])

    history = get_history(target, "name")
    if history.added and history.deleted:
        change["name"] = (history.deleted[0], history.added[0])

    history = get_history(target, "path")
    if history.added and history.deleted:
        change["path"] = (history.deleted[0], history.added[0])

    oldpath = os.path.join(
        config.UPLOAD_FOLDER,
        change["bucket"][0].name,
        change["path"][0].lstrip("/"),
        change["name"][0],
    )
    newpath = os.path.join(
        config.UPLOAD_FOLDER,
        change["bucket"][1].name,
        change["path"][1].lstrip("/"),
        change["name"][1],
    )
    if oldpath != newpath and os.path.exists(oldpath):
        dirname = os.path.dirname(newpath)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        os.rename(oldpath, newpath)

    dirname = os.path.dirname(oldpath)
    if not os.listdir(dirname):
        os.rmdir(dirname)


@event.listens_for(File, 'after_delete')
def file_delete_listen(mapper, connection, target):
    filepath = target.abspath
    if os.path.exists(filepath):
        os.remove(filepath)

    dirname = os.path.dirname(filepath)
    if os.path.exists(dirname) and not os.listdir(dirname):
        os.rmdir(dirname)
