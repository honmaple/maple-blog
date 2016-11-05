#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-15 13:19:04 (CST)
# Last Update:星期六 2016-11-5 23:43:4 (CST)
#          By: jianglin
# Description:
# **************************************************************************
from maple.main.permissions import super_permission
from maple.user.models import User
from maple.extensions import db
from wtforms.validators import DataRequired, Email
from flask import abort, url_for, Markup, request
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_wtf import Form
import os
from os import path as op
from werkzeug import secure_filename
from time import time

file_path = op.join(
    op.dirname(__file__), op.pardir, op.pardir, 'images', 'blog')
try:
    os.mkdir(file_path)
except OSError:
    pass


class BaseForm(Form):
    def __init__(self, formdata=None, obj=None, prefix=u'', **kwargs):
        self._obj = obj
        super(BaseForm, self).__init__(
            formdata=formdata, obj=obj, prefix=prefix, **kwargs)


class BaseModelView(ModelView):

    page_size = 10
    can_view_details = True
    # column_display_pk = True
    form_base_class = BaseForm

    def is_accessible(self):
        return super_permission.can()

    def inaccessible_callback(self, name, **kwargs):
        abort(404)


class BlogView(BaseModelView):
    # column_exclude_list = ['author']
    column_searchable_list = ['title']
    column_filters = ['category', 'created_at']
    form_widget_args = {'content': {'rows': 10}}
    column_formatters = dict(
        content=lambda v, c, m, p: m.content[:100] + '...')
    column_editable_list = ['title', 'category', 'is_copy']
    # inline_models = [Tags]
    form_excluded_columns = ['comments']


class BookView(BaseModelView):
    column_filters = ['tag']


class TagView(BaseModelView):
    column_editable_list = ['name']


class CategoryView(BaseModelView):
    column_editable_list = ['name']


class NoticeView(BaseModelView):
    form_widget_args = {'notice': {'rows': 10}}
    column_filters = ['created_at']


class QueView(BaseModelView):
    column_editable_list = ['title', 'is_private', 'author']
    column_filters = ['is_private', 'created_at']
    column_searchable_list = ['title']


class CommentView(BaseModelView):
    column_editable_list = ['author', 'blog']
    column_filters = ['created_at', 'author']


class UserView(BaseModelView):
    column_searchable_list = ['username']
    column_filters = ['is_confirmed', 'is_superuser']
    column_exclude_list = ['password']
    column_editable_list = ['username', 'is_confirmed', 'is_superuser',
                            'confirmed_time', 'roles']
    form_excluded_columns = ['blogs', 'comments', 'questions']
    form_args = {
        'username': {
            'validators': [DataRequired()]
        },
        'email': {
            'validators': [Email(), DataRequired()]
        }
    }
    form_choices = {
        'roles': [
            ('Super', 'super'), ('Admin', 'admin'), ('Writer', 'writer'),
            ('Vitstor', 'vistor'), ('Guest', 'guest')
        ]
    }

    def create_model(self, form):
        form.password.data = User.set_password(form.password.data)
        super(UserView, self).create_model(form)

# class FileView(BaseModelView):
#     # Override form field to use Flask-Admin FileUploadField
#     form_overrides = {'path': form.FileUploadField}

#     # Pass additional parameters to 'path' to FileUploadField constructor
#     form_args = {
#         'path': {
#             'label': 'File',
#             'base_path': app.static_folder,
#             'allow_overwrite': False
#         }
#     }


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
        model.url = request.url_root + 'images/blog/' + model.path
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
