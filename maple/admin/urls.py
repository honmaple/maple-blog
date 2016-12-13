#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-29 19:27:46 (CST)
# Last Update:星期二 2016-12-13 15:43:48 (CST)
#          By:
# Description:
# **************************************************************************
from maple.user.models import User
from maple.question.models import Question
from maple.books.models import Books
from maple.index.models import Notice
from maple.extensions import admin, db
from .views import (NoticeView, UserView, QueView, BookView)
from .permission import register_permission
from .blog import register_blog
from .file import register_file
from .timeline import register_timeline

admin.add_view(
    NoticeView(
        Notice,
        db.session,
        name='管理公告',
        endpoint='admin_notice',
        url='notices'))
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
admin.add_view(
    BookView(
        Books, db.session, name='管理书籍', endpoint='admin_books', url='books'))
register_blog(admin)
register_permission(admin)
register_file(admin)
register_timeline(admin)
