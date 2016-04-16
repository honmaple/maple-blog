#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-15 13:19:04 (CST)
# Last Update:
#          By:
# Description:
# **************************************************************************
from maple import db, app, redis_data
from maple.main.permissions import super_permission
from maple.user.models import User
from maple.blog.models import Articles
from maple.question.models import Questions
from maple.books.models import Books
from wtforms.validators import DataRequired
from maple.admin.models import Notices, File, Image
from maple.blog.forms import ArticleForm
from flask import Markup, url_for, abort
from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_admin.contrib import rediscli

admin = Admin(app, name='HonMaple后台')


class BaseModelView(ModelView):

    page_size = 10
    can_view_details = True
    form_base_class = SecureForm

    # create_modal = True
    # edit_modal = True
    # can_create = False
    # can_edit = False
    # can_delete = False
    # def is_accessible(self):
    #     if not super_permission.can():
    #         abort(404)


class BlogModelView(BaseModelView):
    column_exclude_list = ['author']
    # form_base_class = ArticleForm
    # form = ArticleForm
    form_widget_args = {'content': {'rows': 10, }}
    # form_columns = ['comments', 'tags']
    # column_labels = dict(title='标题')


class BookModelView(BaseModelView):
    pass


class QueModelView(BaseModelView):
    pass


class UserModelView(BaseModelView):
    column_exclude_list = ['passwd']
    column_searchable_list = ['name', 'email']
    column_editable_list = ['name']
    form_excluded_columns = ['passwd']
    form_args = {'name': {'label': '昵称', 'validators': [DataRequired()]}}


class FileView(ModelView):
    # Override form field to use Flask-Admin FileUploadField
    form_overrides = {'path': form.FileUploadField}

    # Pass additional parameters to 'path' to FileUploadField constructor
    form_args = {
        'path': {
            'label': 'File',
            'base_path': app.static_folder,
            'allow_overwrite': False
        }
    }


class ImageView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        return Markup('<img src="%s">' %
                      url_for('static',
                              filename=form.thumbgen_filename(model.path)))

    column_formatters = {'path': _list_thumbnail}
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=app.static_folder,
                                      thumbnail_size=(100, 100, True))
    }


admin.add_view(UserModelView(User,
                             db.session,
                             name='管理用户',
                             endpoint='admin_user',
                             url='users'))
admin.add_view(ModelView(Questions,
                         db.session,
                         name='管理问题',
                         endpoint='admin_question',
                         url='questions'))
admin.add_view(ModelView(Notices,
                         db.session,
                         name='管理公告',
                         endpoint='admin_notice',
                         url='notices'))
admin.add_view(BlogModelView(Articles,
                             db.session,
                             name='管理文章',
                             endpoint='admin_article',
                             url='articles'))
admin.add_view(BookModelView(Books,
                             db.session,
                             name='管理书籍',
                             endpoint='admin_books',
                             url='books'))
admin.add_view(FileView(File, db.session))
admin.add_view(ImageView(Image, db.session))
admin.add_view(rediscli.RedisCli(redis_data))
