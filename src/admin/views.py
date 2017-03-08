#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-15 13:19:04 (CST)
# Last Update:星期三 2017-3-8 12:50:36 (CST)
#          By: jianglin
# Description:
# **************************************************************************
from api.user.models import User
from wtforms.validators import DataRequired, Email
from flask import abort
from flask_admin.contrib.sqla import ModelView
from flask_wtf import Form
from flask_login import current_user


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
        if current_user.is_authenticated and current_user.is_superuser:
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        abort(404)


class BookView(BaseModelView):
    column_filters = ['tag']


class NoticeView(BaseModelView):
    form_widget_args = {'notice': {'rows': 10}}
    column_filters = ['created_at']


class QueView(BaseModelView):
    column_editable_list = ['title', 'is_private', 'author']
    column_filters = ['is_private', 'created_at']
    column_searchable_list = ['title']


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
