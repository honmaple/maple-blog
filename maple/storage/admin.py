#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: admin.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-06-07 01:40:32 (CST)
# Last Update: Friday 2019-06-28 15:44:05 (CST)
#          By:
# Description:
# ********************************************************************************
from os import path as op

from flask import Markup, url_for
from flask_admin import form
from maple.admin import AdminView
from flask_admin.contrib.sqla import fields as form1
from maple.extension import db

from . import config
from .db import Bucket, FilePath, File
from .util import gen_hash, secure_filename


class BucketView(AdminView):
    column_editable_list = ['name']
    form_excluded_columns = ['paths']
    column_exclude_list = ["updated_at"]


class FilePathView(AdminView):
    column_editable_list = ['name', "bucket"]
    form_excluded_columns = ['files']
    column_exclude_list = ["updated_at"]
    # form_ajax_refs = {'bucket': {'fields': ['name'], 'page_size': 10}}


class FileView(AdminView):
    def _list_thumbnail(view, context, model, name):
        if model.file_type.startswith("image"):
            return Markup('<img src="%s">' % model.url)
        return Markup(
            '<a href="%s" target="_blank">%s</a>' % (model.url, model.name))

    def _prefix_name(obj, file_data):
        part = op.splitext(file_data.filename)
        obj.name = secure_filename('%s%s' % part)
        obj.file_type = file_data.content_type
        obj.hash = gen_hash(file_data)
        file_data.seek(0)
        return obj.relpath

    column_filters = ["file_type", "path.name"]
    column_editable_list = ["name", "path"]
    # column_searchable_list = ["name", "path"]
    column_exclude_list = ["updated_at"]
    column_formatters = {'hash': _list_thumbnail}
    form_excluded_columns = ['hash', "name", "file_type"]

    form_extra_fields = {
        "filename": form.FileUploadField(
            "File",
            namegen=_prefix_name,
            base_path=config.UPLOAD_FOLDER,
            allowed_extensions=config.UPLOAD_ALLOWED_EXTENSIONS,
        )
    }


def init_admin(admin):
    admin.add_view(
        BucketView(
            Bucket,
            db.session,
            name='管理空间',
            endpoint='admin_bucket',
            category='管理存储'))
    admin.add_view(
        FilePathView(
            FilePath,
            db.session,
            name='管理文件夹',
            endpoint='admin_filepath',
            category='管理存储'))
    admin.add_view(
        FileView(
            File,
            db.session,
            name='管理文件',
            endpoint='admin_file',
            category='管理存储'))
