#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: file.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-26 16:14:42 (CST)
# Last Update:星期日 2016-12-4 22:30:19 (CST)
#          By:
# Description:
# **************************************************************************
from .views import BaseModelView
from flask import url_for, Markup, request
from flask_admin import form
import os
from os import path as op
from werkzeug import secure_filename
from time import time
from maple.extensions import db
from maple.index.models import Images

__all__ = ['register_file']

file_path = op.join(
    op.dirname(__file__), op.pardir, op.pardir, 'images', 'blog')
try:
    os.mkdir(file_path)
except OSError:
    pass


def prefix_name(obj, file_data):
    name = str(int(time()))
    part = op.splitext(file_data.filename)[1]
    return secure_filename('blog-%s%s' % (name, part))


class ImageView(BaseModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        return Markup('<img src="%s">' % url_for(
            'images', filename='blog/' + form.thumbgen_filename(model.path)))

    column_formatters = {'path': _list_thumbnail}
    form_excluded_columns = ['url']
    form_extra_fields = {
        'path': form.ImageUploadField(
            'Image',
            base_path=file_path,
            namegen=prefix_name,
            thumbnail_size=(100, 100, True))
    }

    def after_model_change(self, form, model, is_created):
        model.url = request.host_url + 'images/blog/' + model.path
        db.session.commit()

    def after_model_delete(self, model):
        if model.path:
            try:
                os.remove(op.join(file_path, model.path))
            except OSError:
                pass
            try:
                os.remove(
                    op.join(file_path, form.thumbgen_filename(model.path)))
            except OSError:
                pass


def register_file(admin):
    admin.add_view(ImageView(Images, db.session))
