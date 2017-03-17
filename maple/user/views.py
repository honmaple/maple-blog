#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: index.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 02:21:04
# *************************************************************************
from flask import (render_template, redirect, url_for, flash, request,
                   current_app, session, abort)
from flask.views import MethodView
from flask_login import (current_user, login_required, logout_user)
from flask_principal import (AnonymousIdentity, identity_changed)
from maple.user.models import User
from .forms import InforForm, PasswordForm
from flask_maple.form import flash_errors
from functools import wraps


def allow_own(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        name = kwargs.get('name')
        if name is not None and current_user.username != name:
            abort(403)
        return func(*args, **kwargs)

    return decorator


class UserBaseView(MethodView):
    decorators = [allow_own, login_required]


class UserInforView(UserBaseView):
    def __init__(self):
        super(MethodView, self).__init__()
        self.form = InforForm()

    def get(self, name):
        user = User.query.filter_by(username=name).first_or_404()
        self.form.school.data = user.school
        self.form.introduce.data = user.introduce
        data = {'form': self.form, 'user': user}
        return render_template('user/userinfor.html', **data)

    def post(self, name):
        if self.form.validate_on_submit():
            user = User.query.filter_by(username=name).first_or_404()
            user.update_infor(self.form)
            flash('资料更新成功')
            return redirect(url_for('user.infor', name=user.username))
        else:
            if self.form.errors:
                flash_errors(self.form)
            return redirect(url_for('user.infor', name=name))


class UserPasswordView(UserBaseView):
    def __init__(self):
        super(MethodView, self).__init__()
        self.form = PasswordForm()

    def get(self, name):
        user = User.query.filter_by(username=name).first_or_404()
        data = {'form': self.form, 'user': user}
        return render_template('user/userpassword.html', **data)

    def post(self, name):
        if self.form.validate_on_submit():
            user = User.query.filter_by(username=name).first()
            password = self.form.passwd.data
            if user.check_password(password):
                user.update_password(self.form.new_passwd.data)
                flash('密码修改成功,请重新登陆')
                logout_user()
                for key in ('identity.id', 'identity.auth_type'):
                    session.pop(key, None)
                identity_changed.send(
                    current_app._get_current_object(),
                    identity=AnonymousIdentity())
                return redirect(url_for('auth.login'))
            else:
                flash('密码错误，请重新输入')
                return redirect(
                    url_for(
                        'user.password', name=current_user.username))
        else:
            if self.form.errors:
                flash_errors(self.form)
            return redirect(url_for('user.password', name=name))


class UserBlogListView(UserBaseView):
    def get(self, name):
        page = request.args.get('page', 1, type=int)
        user = User.query.filter_by(username=name).first_or_404()
        blogs = user.blogs.paginate(page, 20, True)
        data = {'blogs': blogs}
        return render_template('user/bloglist.html', **data)


class UserCommentListView(UserBaseView):
    def get(self, name):
        page = request.args.get('page', 1, type=int)
        user = User.query.filter_by(username=name).first_or_404()
        comments = user.comments.paginate(page, 20, True)
        data = {'comments': comments}
        return render_template('user/commentlist.html', **data)


class UserQueListView(UserBaseView):
    def get(self, name):
        page = request.args.get('page', 1, type=int)
        user = User.query.filter_by(username=name).first_or_404()
        questions = user.questions.paginate(page, 20, True)
        data = {'questions': questions}
        return render_template('user/quelist.html', **data)
