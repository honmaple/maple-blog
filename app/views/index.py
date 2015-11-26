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
    url_for,session,flash
from ..models import User, db
# from ..models import Books
# from ..forms import UserForm
from app import register_pages

site = Blueprint('index',__name__,url_prefix='')

flatpages = register_pages()

@site.route('/')
@site.route('/index')
def index():
    pages = (p for p in flatpages if 'Date' in p.meta)
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['Date'])
    return render_template('index/index.html',
                           pages = latest[:6])

@site.route('/login', methods=['GET','POST'])
def login():
    return redirect(url_for('index.index'))
    # name = None
    # error = None
    # form = UserForm()
    # if form.validate_on_submit():
            # name = form.name.data
            # form.name.data=''
    # if request.method == 'POST':
        # user = User.query.filter_by(name=request.form['name']).first()
        # if user != None:
            # if request.form['passwd'] != user.passwd:
                # error = u'密码错误'
            # else:
                # session['logged_in'] = True
                # flash('You were logged in')
                # return redirect(url_for('admin.index'))
        # else:
            # error = u'用户名错误'
    # return render_template('admin/login.html',form=form,name=name,error=error)

@site.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index.index'))

@site.route('/sign', methods=['GET','POST'])
def sign():
    return redirect(url_for('index.index'))
    # name = None
    # error = None
    # form = UserForm()
    # if form.validate_on_submit():
            # name = form.name.data
            # form.name.data=''
    # if request.method == 'POST':
        # useremail = User.query.filter_by(email=request.form['email']).first()
        # username = User.query.filter_by(name=request.form['name']).first()
        # if username:
            # error = u'用户名已存在'
        # elif useremail:
            # error = u'邮箱已被注册'
        # elif not request.form['name'] or not request.form['email']:
            # error = u'输入不能为空'
        # else:
            # account = User(request.form['name'],request.form['email'],request.form['passwd'])
            # db.session.add(account)
            # db.session.commit()
            # session['logged_in'] = True
            # flash('You were logged in')
            # return redirect(url_for('admin.index'))
    # return render_template('admin/sign_in.html',form=form,name=name,error=error)

@site.route('/about')
def about():
    return render_template('index/about_me.html')

