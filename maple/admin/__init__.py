# !/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-11 17:35:11 (CST)
# Last Update: 星期四 2018-01-25 13:41:50 (CST)
#          By:
# Description:
# **************************************************************************
from flask_admin import Admin
from maple.model import User
from maple.model import Question
from maple.extension import db
from maple.admin import blog, file, timeline
from .views import (UserView, QueView)

admin = Admin(name='HonMaple', template_mode='bootstrap3')

admin.add_view(
    UserView(
        User, db.session, name='管理用户', endpoint='admin_user', url='users'))
admin.add_view(
    QueView(
        Question,
        db.session,
        name='管理问题',
        endpoint='admin_question',
        url='questions'))

blog.init_admin(admin)
file.init_admin(admin)
timeline.init_admin(admin)


def init_app(app):
    admin.index_view.url = app.config['ADMIN_URL']
    admin.init_app(app)
