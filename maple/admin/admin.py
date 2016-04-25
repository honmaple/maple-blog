#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-15 13:19:04 (CST)
# Last Update: 星期一 2016-4-25 18:57:48 (CST)
#          By: jianglin
# Description:
# **************************************************************************
from maple import db, app
from maple.main.permissions import super_permission
from maple.user.models import User
from maple.blog.models import Articles
from maple.question.models import Questions
from maple.books.models import Books
from wtforms.validators import DataRequired
from maple.admin.models import Notices
from flask import abort
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import Form


admin = Admin(app, name='HonMaple', template_mode='bootstrap3')


class BaseModelView(ModelView):

    page_size = 10
    can_view_details = True
    form_base_class = Form

    def is_accessible(self):
        return super_permission.can()

    def inaccessible_callback(self, name, **kwargs):
        abort(404)


class BlogModelView(BaseModelView):
    column_exclude_list = ['author']
    column_filters = ['category', 'publish']
    form_widget_args = {'content': {'rows': 10}}
    column_formatters = dict(
        content=lambda v, c, m, p: m.content[:100] + '...')
    column_editable_list = ['title', 'category']
    form_excluded_columns = ['comments']
    form_choices = {'category': [('Linux', 'linux'),
                                 ('Python', 'python'),
                                 ('生活随笔', '生活随笔')],
                    'author': [('honmaple', 'honmaple')]}


class BookModelView(BaseModelView):
    column_filters = ['tag']


class NoticeModelView(BaseModelView):
    form_widget_args = {'notice': {'rows': 10}}
    column_filters = ['publish']


class QueModelView(BaseModelView):
    column_editable_list = ['title', 'private']
    column_filters = ['private', 'publish']
    form_choices = {'author': [('honmaple', 'honmaple')]}


class UserModelView(BaseModelView):
    column_exclude_list = ['passwd']
    column_editable_list = ['name', 'is_confirmed', 'is_superuser',
                            'confirmed_time', 'roles']
    form_excluded_columns = ['passwd']
    form_args = {'name': {'validators': [DataRequired()]}}
    form_choices = {
        'roles': [
            ('Super', 'super'), ('Admin', 'admin'), ('Writer', 'writer'),
            ('Vitstor', 'vistor'), ('Guest', 'guest')
        ]
    }


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


# class ImageView(BaseModelView):

#     def _list_thumbnail(view, context, model, name):
#         if not model.path:
#             return ''
#         return Markup('<img src="%s">' %
#                       url_for('static',
#                               filename=form.thumbgen_filename(model.path)))

#     column_formatters = {'path': _list_thumbnail}
#     form_extra_fields = {
#         'path': form.ImageUploadField('Image',
#                                       base_path=app.static_folder,
#                                       thumbnail_size=(100, 100, True))
#     }


admin.add_view(UserModelView(User,
                             db.session,
                             name='管理用户',
                             endpoint='admin_user',
                             url='users'))
admin.add_view(QueModelView(Questions,
                            db.session,
                            name='管理问题',
                            endpoint='admin_question',
                            url='questions'))
admin.add_view(NoticeModelView(Notices,
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
# admin.add_view(FileView(File, db.session))
# admin.add_view(ImageView(Image, db.session))
