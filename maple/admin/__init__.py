# !/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-04-11 17:35:11 (CST)
# Last Update: Friday 2019-06-07 15:37:08 (CST)
#          By:
# Description:
# **************************************************************************
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_babel import lazy_gettext as _
from werkzeug import import_string


def init_app(app):
    admin = Admin(
        name=_("honmaple"),
        index_view=AdminIndexView(
            template="admin/index.html",
            url=app.config.get("ADMIN_URL", "/"),
        ),
        template_mode="bootstrap3")

    init_admin(admin)
    admin.init_app(app)


def init_admin(admin):
    admins = [
        "maple.admin.views",
        "maple.admin.blog",
        "maple.admin.timeline",
        "maple.storage.admin",
    ]
    [import_string(i).init_admin(admin) for i in admins]
