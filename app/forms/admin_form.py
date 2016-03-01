#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: administrator.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 21:58:14
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField,\
    SelectField,TextAreaField
from wtforms.validators import Required,Length,EqualTo


class EditUserInforForm(Form):
    introduce = TextAreaField('个人介绍',
                              [Required(message='个人介绍不能为空')])
    school = StringField('学校/公司',
                         [Required(message='学校/公司不能为空')])

class EditPasswdForm(Form):
    passwd = PasswordField('密码',
                           [Required(message='密码输入不能为空')])
    new_passwd = PasswordField('新密码',
                               [Required(message=u'新密码不能为空'),
                                Length(min=4,
                                       max=20,
                                       message='密码长度在4到20个字符之间'),
                                EqualTo('retry_new_passwd',
                                        message=u'两次密码不一致')])
    retry_new_passwd = PasswordField('重复新密码',
                                     [Required(message=u'重复密码不能为空')])

class EditRegisterForm(Form):
    name = StringField('用户名', [Length(min=4, max=25)])
    is_superuser = SelectField('是否授予超级管理员权限',
                           choices=[('True','True'), ('False', 'False')],
                           validators=[Required()])
    roles = SelectField('用户组',
                           choices=[('super','Super'),('admin', 'Admin'),
                                    ('writer', 'Writer'),('editor','Editor'),
                                    ('visitor','Visitor')],
                           validators=[Required()])
    is_confirmed = SelectField('修改用户验证状态',
                               choices=[('True','True'), ('False', 'False')],
                               validators=[Required()])
    edit = SubmitField('修改')

class NoticesForm(Form):
    notice = TextAreaField('公告内容', [Required()])
    confirm = SubmitField('发布公告')

# class SearchForm(Form):
    # search = StringField('搜索', [Required()])
