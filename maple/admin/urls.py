#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-29 19:27:46 (CST)
# Last Update:星期六 2016-11-5 22:28:38 (CST)
#          By:
# Description:
# **************************************************************************
from maple.user.models import User
from maple.blog.models import Blog, Comment, Tags, Category
from maple.question.models import Question
from maple.books.models import Books
from maple.index.models import Notice, Images
from maple.extensions import admin, db
from .views import (NoticeView, UserView, QueView, BookView, CategoryView,
                    BlogView, TagView, CommentView, ImageView)

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
    BlogView(
        Blog,
        db.session,
        name='管理文章',
        endpoint='admin_article',
        url='articles'))
admin.add_view(
    CategoryView(
        Category,
        db.session,
        name='管理分类',
        endpoint='admin_category',
        url='categories'))
admin.add_view(
    TagView(
        Tags, db.session, name='管理节点', endpoint='admin_tag', url='tags'))
admin.add_view(
    CommentView(
        Comment,
        db.session,
        name='管理回复',
        endpoint='admin_comment',
        url='comments'))
admin.add_view(
    BookView(
        Books, db.session, name='管理书籍', endpoint='admin_books', url='books'))
# admin.add_view(FileView(File, db.session))
admin.add_view(ImageView(Images, db.session))
