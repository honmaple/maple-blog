#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: index.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 02:21:04
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint,redirect, \
    url_for,session,flash,request,g,abort
from flask.ext.login import login_user, logout_user, \
    current_user, login_required
import datetime
from werkzeug.security import check_password_hash
from ..email import email_token,email_send,confirm_token,\
    email_validate
from app import login_manager
from app import register_pages
from ..models import User,Articledb,db
from ..forms import LoginForm,RegisterForm

site = Blueprint('index',__name__,url_prefix='')

flatpages = register_pages()


@site.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))

@site.route('/')
@site.route('/index')
def index():
    return render_template('index/index.html')

@site.route('/login', methods=['GET','POST'])
def login():
    error = None
    form = LoginForm()
    if g.user is not None and g.user.is_authenticated:
        flash('你已经登陆,不能重复登陆')
        return redirect(url_for('index.index'))
    if request.method == 'POST':
        user = User.query.filter_by(name=form.name.data).first()
        if user:
            if not check_password_hash(user.passwd, form.passwd.data):
                error = u'密码错误'
            else:
                login_user(user)
                flash('你已成功登陆.')
                '''next是必需的,登陆前请求的页面'''
                return redirect(url_for('index.index'))
        else:
            error = u'用户名错误'
    return render_template('index/login.html',
                           form=form,
                           error = error)

@site.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))


@site.route('/sign', methods=['GET','POST'])
def sign():
    error = None
    form = RegisterForm()
    if g.user is not None and g.user.is_authenticated:
        flash('你已经登陆,不能重复登陆')
        return redirect(url_for('index.index'))
    if request.method == 'POST':
        useremail = User.query.filter_by(email=form.email.data).first()
        username = User.query.filter_by(name=form.name.data).first()
        email_format = email_validate(form.email.data)
        print(email_format)
        if username:
            error = u'用户名已存在'
        elif useremail:
            error = u'邮箱已被注册'
        elif email_format == False:
            error = u'邮箱格式错误'
        elif not form.name.data or not form.email.data:
            error = u'输入不能为空'
        else:
            account = User(name = form.name.data,
                           email = form.email.data,
                           passwd = form.passwd.data,
                           confirmed = False)
            db.session.add(account)
            db.session.commit()

            '''邮箱验证'''
            token = email_token(account.email)
            login_user(account)
            print(token)
            '''email模板'''
            confirm_url = url_for('index.confirm', token=token, _external=True)
            html = render_template('email.html', confirm_url=confirm_url)
            email_send(account.email,html)

            flash('一封验证邮件已发往你的邮箱，請查收.', 'success')
            return redirect(url_for('index.logined_user',name=account.name))
    return render_template('index/sign_in.html',form=form,error=error)

@site.route('/confirm/<token>')
@login_required
def confirm(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('账户已经验证. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('index.logined_user',name=user.name))

@site.route('/u/<name>/view?')
@login_required
def logined_user(name):
    user_questions = Articledb.query.filter_by(name=name).all()
    user = User.query.filter_by(name=name).first()
    email = user.email
    confirmed = user.confirmed
    registered_on = user.registered_on
    form = LoginForm()
    return render_template('user/user.html',
                            name = name,
                            email = email,
                            confirmed = confirmed,
                            registered_on = registered_on,
                            form = form,
                            user_questions = user_questions)

# @site.route('/u/<name>/delete?question=<title>')
# def ask_delete(name,title):
    # db.session.delete(title=title)

@site.route('/about')
def about():
    return render_template('index/about_me.html')

