#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-04-15 13:19:04 (CST)
# Last Update:星期一 2016-10-3 21:38:53 (CST)
#          By: jianglin
# Description:
# **************************************************************************
from maple import db, app
from maple.main.permissions import super_permission
from maple.user.models import User
from maple.blog.models import Blog, Comment, Tags,Category
from maple.question.models import Question
from maple.books.models import Books
from wtforms.validators import DataRequired
from maple.index.models import Notice
from flask import abort
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import Form

admin = Admin(app,
              name='HonMaple',
              url=app.config.get('ADMIN_URL', '/admin'),
              template_mode='bootstrap3')


class BaseForm(Form):
    def __init__(self, formdata=None, obj=None, prefix=u'', **kwargs):
        self._obj = obj
        super(BaseForm, self).__init__(formdata=formdata,
                                       obj=obj,
                                       prefix=prefix,
                                       **kwargs)


class BaseModelView(ModelView):

    page_size = 10
    can_view_details = True
    form_base_class = BaseForm

    # def is_accessible(self):
    #     return super_permission.can()

    # def inaccessible_callback(self, name, **kwargs):
    #     abort(404)


class BlogModelView(BaseModelView):
    # column_exclude_list = ['author']
    column_searchable_list = ['title']
    column_filters = ['category', 'created_at']
    form_widget_args = {'content': {'rows': 10}}
    column_formatters = dict(
        content=lambda v, c, m, p: m.content[:100] + '...')
    column_editable_list = ['title', 'category']
    form_excluded_columns = ['comments']
    form_choices = {'category': [('Linux', 'Linux'), ('Python', 'Python'),
                                 ('生活随笔', '生活随笔'), ('Security', 'Web安全'),
                                 ('HTML', 'Web前端')],
                    'author': [('honmaple', 'honmaple')]}


class BookModelView(BaseModelView):
    column_filters = ['tag']


class TagModelView(BaseModelView):
    pass

class CategoryModelView(BaseModelView):
    pass


class NoticeModelView(BaseModelView):
    form_widget_args = {'notice': {'rows': 10}}
    column_filters = ['created_at']


class QueModelView(BaseModelView):
    column_editable_list = ['title', 'is_private']
    column_filters = ['is_private', 'created_at']
    form_choices = {'author': [('honmaple', 'honmaple')]}


class CommentModelView(BaseModelView):
    column_filters = ['created_at', 'author']


class UserModelView(BaseModelView):
    column_exclude_list = ['passwd']
    column_editable_list = ['username', 'is_confirmed', 'is_superuser',
                            'confirmed_time', 'roles']
    form_excluded_columns = ['passwd']
    form_args = {'username': {'validators': [DataRequired()]}}
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
admin.add_view(QueModelView(Question,
                            db.session,
                            name='管理问题',
                            endpoint='admin_question',
                            url='questions'))
admin.add_view(NoticeModelView(Notice,
                               db.session,
                               name='管理公告',
                               endpoint='admin_notice',
                               url='notices'))
admin.add_view(BlogModelView(Blog,
                             db.session,
                             name='管理文章',
                             endpoint='admin_article',
                             url='articles'))
admin.add_view(CategoryModelView(Category,
                                 db.session,
                                 name='管理分类',
                                 endpoint='admin_category',
                                 url='categories'))
admin.add_view(TagModelView(Tags,
                            db.session,
                            name='管理节点',
                            endpoint='admin_tag',
                            url='tags'))
admin.add_view(CommentModelView(Comment,
                                db.session,
                                name='管理回复',
                                endpoint='admin_comment',
                                url='comments'))
admin.add_view(BookModelView(Books,
                             db.session,
                             name='管理书籍',
                             endpoint='admin_books',
                             url='books'))
# admin.add_view(FileView(File, db.session))
# admin.add_view(ImageView(Image, db.session))
