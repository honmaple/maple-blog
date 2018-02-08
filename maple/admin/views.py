#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-15 13:19:04 (CST)
# Last Update: 星期五 2018-02-09 17:06:24 (CST)
#          By: jianglin
# Description:
# **************************************************************************
from maple.model import User
from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField
from wtforms.validators import DataRequired, Email, Length


class AdminView(ModelView):

    page_size = 10
    can_view_details = True
    # column_display_pk = True
    # form_base_class = BaseForm

    # def is_accessible(self):
    #     return current_user.is_authenticated and current_user.is_superuser is True

    # def inaccessible_callback(self, name, **kwargs):
    #     abort(404)


class NoticeView(AdminView):
    form_widget_args = {'notice': {'rows': 10}}
    column_filters = ['created_at']


class QueView(AdminView):
    column_editable_list = ['title', 'is_hidden', 'user']
    column_filters = ['is_hidden', 'created_at']
    column_searchable_list = ['title']


class UserView(AdminView):
    column_searchable_list = ['username']
    column_filters = ['is_confirmed', 'is_superuser']
    column_exclude_list = ['password']
    column_editable_list = ['username', 'is_confirmed', 'is_superuser']
    form_excluded_columns = ['blogs', 'comments', 'questions']
    form_args = {
        'username': {
            'validators': [DataRequired()]
        },
        'email': {
            'validators': [Email(), DataRequired()]
        }
    }

    def scaffold_form(self):
        form_class = super(UserView, self).scaffold_form()
        form_class.password = PasswordField(
            "Password", [DataRequired(), Length(
                min=4, max=20)])
        return form_class

    def create_model(self, form):
        user = User()
        user.set_password(form.password.data)
        form.password.data = user.password
        return super(UserView, self).create_model(form)

    def update_model(self, form, model):
        form.password.data = model.set_password(form.password.data)
        return super(UserView, self).update_model(form, model)
