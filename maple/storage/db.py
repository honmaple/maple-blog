#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: db.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:05 (CST)
# Last Update: Saturday 2019-07-20 12:35:33 (CST)
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
from werkzeug.utils import secure_filename

from . import config


class Bucket(ModelUserMixin, db.Model):
    __tablename__ = 'bucket'

    name = db.Column(db.String(108), nullable=False, unique=True)
    description = db.Column(db.String(1024), default='default')

    def get_root_path(self, path, create=False):
        filepath = self.rootpath
        for name in path.split("/"):
            if name == "":
                continue
            childpath = filepath.child_paths.filter_by(
                name=name,
                bucket_id=self.id,
            ).first()
            if not childpath and not create:
                return

            if not childpath and create:
                childpath = FilePath(
                    name=name,
                    bucket_id=self.id,
                    parent_id=filepath.id,
                )
                childpath.save()
            filepath = childpath
        return filepath

    @property
    def rootpath(self):
        filepath = self.paths.filter_by(name="/").first()
        if not filepath:
            filepath = FilePath(name="/", bucket_id=self.id)
            filepath.save()
        return filepath

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

    @property
    def size(self):
        size = sum(
            [
                i[0] for i in db.session.query(File.size).filter_by(
                    path_id=self.id)
            ])
        return size + sum([i.size for i in self.child_paths])

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
    def fullname(self):
        if self.is_root_path:
            return "/"
        return os.path.join(
            self.parent_path.fullname,
            self.name,
        )

    @property
    def is_root_path(self):
        return self.name == "/" and not self.parent_id

    @property
    def is_dir(self):
        return True

    def rename(self, newname):
        newname = secure_filename(newname)
        self.name = newname
        self.save()
        return self

    def move(self, newpath):
        filepath = newpath.child_paths.filter_by(name=self.name).first()
        if not filepath:
            self.parent_id = newpath.id
            self.save()
            return self
        for fp in self.child_paths:
            fp.move(filepath)
        for f in self.files:
            f.move(filepath)
        self.delete()
        return filepath

    def copy(self, newpath):
        # TODO: 性能优化
        filepath = newpath.child_paths.filter_by(name=self.name).first()
        if not filepath:
            filepath = FilePath(
                name=self.name,
                bucket_id=self.bucket_id,
                parent_id=newpath.id,
            )
            filepath.save()
        for fp in self.child_paths:
            fp.copy(filepath)
        for f in self.files:
            f.copy(filepath)
        return filepath

    def __str__(self):
        if self.is_root_path:
            return self.name
        return os.path.join(
            self.parent_path.__str__(),
            self.name,
        )


class File(ModelTimeMixin, db.Model):
    __tablename__ = 'file'

    FILE_TYPE = ("IMAGE", "CSS", "JS")
    FILE_IMAGE = "IMAGE"

    name = db.Column(db.String(108), nullable=False)
    file_type = db.Column(db.String(108), nullable=False)
    hash = db.Column(db.String(1024), nullable=False)
    size = db.Column(db.Integer, nullable=False, default=0)

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
        args = dict(filename=self.relpath, _external=True)
        if config.HTTPS:
            args.update(**dict(_scheme="https"))
        if self.file_type.startswith("image"):
            args.update(type="mini")
        return url_for("storage.show", **args)

    @property
    def is_dir(self):
        return False

    def save(self):
        self.name = self.name.strip("/")
        if "/" in self.name:
            s = self.name.split("/")
            filepath = FilePath.query.filter_by(id=self.path_id).first()
            filepath = filepath.bucket.get_root_path("/".join(s[:-1]), True)
            self.name = s[-1]
            self.path_id = filepath.id
        return super(File, self).save()

    def copy(self, newpath):
        f = File(
            name=self.name,
            file_type=self.file_type,
            hash=self.hash,
            path_id=newpath.id,
        )
        f.save()
        return f

    def move(self, newpath):
        self.path_id = newpath
        self.save()
        return self

    def rename(self, newname):
        newname = secure_filename(newname)
        self.name = newname
        self.save()
        return self

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
