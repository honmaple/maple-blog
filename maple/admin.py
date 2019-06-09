# !/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016-2019 jianglin
# File Name: admin.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-04-11 17:35:11 (CST)
# Last Update: Sunday 2019-06-16 15:06:04 (CST)
#          By:
# Description:
# **************************************************************************
from flask import abort
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_babel import lazy_gettext as _
from flask_login import current_user
from flask_wtf import FlaskForm as Form
from maple.extension import db
from maple.model import User
from werkzeug import import_string
from wtforms import PasswordField
from wtforms.validators import DataRequired, Email, Length


class BaseForm(Form):
    def __init__(self, formdata=None, obj=None, prefix=u'', **kwargs):
        self._obj = obj
        super(BaseForm, self).__init__(
            formdata=formdata, obj=obj, prefix=prefix, **kwargs)


class AdminView(ModelView):

    page_size = 10
    can_view_details = True
    form_base_class = BaseForm

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_superuser

    def inaccessible_callback(self, name, **kwargs):
        abort(404)


class UserView(AdminView):
    column_searchable_list = ['username']
    column_filters = ['is_confirmed', 'is_superuser']
    column_exclude_list = ['password']
    column_editable_list = ['username', 'is_confirmed', 'is_superuser']
    form_excluded_columns = ['articles', 'comments']
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
            "Password", [DataRequired(), Length(min=4, max=20)])
        return form_class

    def create_model(self, form):
        user = User()
        user.set_password(form.password.data)
        form.password.data = user.password
        return super(UserView, self).create_model(form)

    # def update_model(self, form, model):
    #     form.password.data = model.set_password(form.password.data)
    #     return super(UserView, self).update_model(form, model)


def init_app(app):
    admin = Admin(
        name=_("honmaple"),
        index_view=AdminIndexView(
            template="admin/index.html",
            url=app.config.get("ADMIN_URL", "/"),
        ),
        template_mode="bootstrap3")

    admins = [
        "maple.admin",
        "maple.blog.admin",
        "maple.storage.admin",
    ]
    [import_string(i).init_admin(admin) for i in admins]
    admin.init_app(app)


def init_admin(admin):
    admin.add_view(
        UserView(
            User,
            db.session,
            name='管理用户',
            endpoint='admin_user',
        ))
