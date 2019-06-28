#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: db.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:05 (CST)
# Last Update: Sunday 2019-06-30 15:19:19 (CST)
#          By:
# Description:
# ********************************************************************************
import os

from flask_maple.models import ModelTimeMixin, ModelUserMixin
from flask import url_for
from maple.extension import db
from sqlalchemy import event
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm.attributes import get_history

from . import config


class Bucket(ModelUserMixin, db.Model):
    __tablename__ = 'bucket'

    name = db.Column(db.String(108), nullable=False, unique=True)
    description = db.Column(db.String(1024), default='default')

    # @property
    # def images(self):
    #     return self.files.filter_by(file_type=File.FILE_IMAGE)

    @property
    def abspath(self):
        return os.path.join(config.UPLOAD_FOLDER, self.name)

    @property
    def relpath(self):
        return os.path.join(self.name)

    def __repr__(self):
        return '<Bucket %r>' % self.name

    def __str__(self):
        return self.name


class FilePath(ModelTimeMixin, db.Model):
    __tablename__ = 'filepath'

    name = db.Column(db.String(108), nullable=False, default="/")

    bucket_id = db.Column(
        db.Integer,
        db.ForeignKey('bucket.id', ondelete="CASCADE"),
        nullable=False)
    bucket = db.relationship(
        Bucket,
        backref=db.backref(
            'paths',
            cascade='all,delete-orphan',
            lazy='dynamic',
        ),
        lazy='joined',
        uselist=False)

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey('filepath.id', ondelete="CASCADE"),
    )

    @declared_attr
    def parent_path(cls):
        return db.relationship(
            'FilePath',
            remote_side=[cls.id],
            backref=db.backref(
                'child_paths',
                remote_side=[cls.parent_id],
                cascade='all,delete-orphan',
                lazy='dynamic'),
            lazy='joined',
            uselist=False)

    @property
    def abspath(self):
        if self.is_root_path:
            return self.bucket.abspath
        return os.path.join(
            self.parent_path.abspath,
            self.name,
        )

    @property
    def relpath(self):
        if self.is_root_path:
            return self.bucket.relpath
        return os.path.join(
            self.parent_path.relpath,
            self.name,
        )

    @property
    def is_root_path(self):
        return self.name == "/" and not self.parent_id

    @classmethod
    def check(cls, name, filepath):
        bucket_id = filepath.bucket_id
        for path in name.split("/"):
            if path == "":
                continue
            childpath = FilePath.query.filter_by(
                name=path,
                bucket_id=bucket_id,
            ).first()
            if not childpath:
                childpath = FilePath(
                    name=path,
                    parent_id=filepath.id,
                    bucket_id=bucket_id,
                )
                childpath.save()
            filepath = childpath
        return filepath

    def __str__(self):
        if self.is_root_path:
            return self.name
        return "/" + self.name


class File(ModelTimeMixin, db.Model):
    __tablename__ = 'file'

    FILE_TYPE = ("IMAGE", "CSS", "JS")
    FILE_IMAGE = "IMAGE"

    name = db.Column(db.String(108), nullable=False)
    file_type = db.Column(db.String(108), nullable=False)
    hash = db.Column(db.String(1024), nullable=False)

    path_id = db.Column(
        db.Integer,
        db.ForeignKey('filepath.id', ondelete="CASCADE"),
        nullable=False)
    path = db.relationship(
        FilePath,
        backref=db.backref(
            'files', cascade='all,delete-orphan', lazy='dynamic'),
        lazy='joined',
        uselist=False)

    @property
    def abspath(self):
        return os.path.join(
            self.path.abspath,
            self.name,
        )

    @property
    def relpath(self):
        return os.path.join(
            self.path.relpath,
            self.name,
        )

    @property
    def url(self):
        args = dict(filename=self.relpath)
        if config.HTTPS:
            args.update(**dict(_external=True, _scheme="https"))
        if self.file_type.startswith("image"):
            args.update(type="mini")
        return url_for("storage.show", **args)

    def save(self):
        s = self.name.split("/")
        self.name = s[-1]
        filepath = FilePath.query.filter_by(id=self.path_id).first()
        filepath = FilePath.check("/".join(s[:-1]), filepath)
        self.path_id = filepath.id
        return super(File, self).save()

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
    if os.path.exists(filepath):
        os.rmdir(filepath)


@event.listens_for(FilePath, 'after_update')
def filepath_update_listen(mapper, connection, target):
    change = {
        "name": (target.name, target.name),
        "bucket": (target.bucket, target.bucket)
    }
    history = get_history(target, "bucket")
    if history.added and history.deleted:
        change["bucket"] = (history.deleted[0], history.added[0])

    history = get_history(target, "name")
    if history.added and history.deleted:
        change["name"] = (history.deleted[0], history.added[0])

    oldpath = os.path.join(
        change["bucket"][0].abspath,
        change["name"][0],
    )
    newpath = os.path.join(
        change["bucket"][1].abspath,
        change["name"][1],
    )
    if oldpath != newpath and os.path.exists(oldpath):
        os.rename(oldpath, newpath)


@event.listens_for(File, 'after_update')
def file_update_listen(mapper, connection, target):
    change = {
        "name": (target.name, target.name),
        "path": (target.path, target.path),
        "hash": (target.hash, target.hash),
    }
    history = get_history(target, "hash")
    if history.added and history.deleted:
        change["hash"] = (history.deleted[0], history.added[0])

    history = get_history(target, "name")
    if history.added and history.deleted:
        change["name"] = (history.deleted[0], history.added[0])

    history = get_history(target, "path")
    if history.added and history.deleted:
        change["path"] = (history.deleted[0], history.added[0])

    oldpath = os.path.join(
        change["path"][0].abspath,
        change["name"][0],
    )
    newpath = os.path.join(
        change["path"][1].abspath,
        change["name"][1],
    )
    file_change = change["hash"][0] != change["hash"][1]
    filepath_change = oldpath != newpath and os.path.exists(oldpath)

    if file_change and filepath_change:
        os.remove(oldpath)

    if not file_change and filepath_change:
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
