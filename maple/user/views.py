#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: index.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 02:21:04
# *************************************************************************
from flask import (render_template, Blueprint, redirect, url_for, flash,
                   request, current_app, session, abort)
from flask_login import (current_user, login_required, logout_user)
from flask_principal import (AnonymousIdentity, identity_changed)
from werkzeug.security import check_password_hash
from maple import cache
from maple.user.models import User
from maple.question.models import Questions
from maple.blog.models import Comments
from maple.user.forms import EditPasswdForm, EditUserInforForm
from flask_maple.forms import return_errors
from maple.main.manager import EditManager
from maple.main.permissions import writer_permission
from flask import jsonify

site = Blueprint('user', __name__)


@site.route('/<name>')
@login_required
@cache.cached(timeout=180)
def logined_user(name):
    '''不能进别人主页'''
    if current_user.username != name:
        abort(404)
    user_questions = Questions.query.filter_by(author=name)
    user_comments = Comments.query.filter_by(author=name).limit(16)
    user = User.query.filter_by(username=name).first()
    form = EditUserInforForm()
    new_passwd_form = EditPasswdForm()
    return render_template('user/user.html',
                           form=form,
                           user=user,
                           new_passwd_form=new_passwd_form,
                           user_comments=user_comments,
                           user_questions=user_questions)


@site.route('/<post_id>/edit?information', methods=['GET', 'POST'])
@login_required
def user_infor_edit(post_id):
    error = None
    form = EditUserInforForm()
    action = EditManager(post_id, form)
    user = User.query.filter_by(id=post_id).first()
    if not form.school.data:
        form.school.data = user.school
    if not form.introduce.data:
        form.introduce.data = user.introduce
    if form.validate_on_submit() and request.method == "POST":
        action.edit_user_infor()
        error = u'资料更新成功'
        return jsonify(judge=True, error=error)
    else:
        if form.errors:
            return return_errors(form)
        else:
            pass
        return redirect(url_for('index.index'))


@site.route('/<post_id>/edit?password', methods=['GET', 'POST'])
@login_required
def user_passwd_edit(post_id):
    error = None
    # if not writer_permission.can():
    #     error = u'你没有验证账户，不能修改密码，请尽快验证账户.'
    #     return jsonify(judge=False, error=error)
    form = EditPasswdForm()
    action = EditManager(post_id, form)
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(id=post_id).first()
        if check_password_hash(user.password, form.passwd.data):
            action.edit_user_passwd()
            flash('密码修改成功,请重新登陆')
            logout_user()
            for key in ('identity.id', 'identity.auth_type'):
                session.pop(key, None)
            identity_changed.send(current_app._get_current_object(),
                                  identity=AnonymousIdentity())
            error = "密码修改"
            return jsonify(judge=True, error=error)
        else:
            error = u'密码错误，请重新输入'
            return jsonify(judge=False, error=error)
    else:
        if form.errors:
            return return_errors(form)
        else:
            pass
        return redirect(url_for('index.index'))
