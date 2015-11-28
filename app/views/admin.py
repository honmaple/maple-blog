#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint, request, \
    session, flash, redirect, url_for
from ..models import MarkDown,User, db
from ..forms import MkdsForm, AdminForm

site = Blueprint('admin',__name__,url_prefix='/admin')

@site.route('/')
def index():
    return redirect(url_for('index.index'))
#    return render_template('admin/admin.html')

@site.route('/login_in',methods=['GET','POST'])
def login():
    return redirect(url_for('index.index'))
    # error = None
    # form = AdminForm()
    # if form.validate_on_submit():
            # name = form.name.data
            # form.name.data=''
    # if request.method == 'POST':
        # if request.form['name'] == 'jianglin':
            # if request.form['passwd'] != 'hello':
                # error = u'密码错误'
            # else:
                # session['logged_in'] = True
                # flash('You were logged in')
                # return redirect(url_for('admin.index'))
        # else:
            # error = u'用户名错误'
    # return render_template('admin/login.html',form = form,
                           # error = error)

@site.route('/logout')
def logout():
    return redirect(url_for('index.index'))
    # session.pop('logged_in', None)
    # flash('You were logged out')
    # return redirect(url_for('index.index'))

@site.route('/pages_post', methods=['GET','POST'])
def pages():
    return redirect(url_for('index.index'))
    # mkds = MarkDown.query.all()
    # form = MkdsForm()
    # if form.validate_on_submit():
    # # if request.method == 'POST':
        # pager = MarkDown(request.form['title'],request.form['datetime'], \
                     # request.form['category'],request.form['tags'], \
                     # request.form['summary'],request.form['body'])
        # db.session.add(pager)
        # db.session.commit()
        # session['post_in'] = True
        # flash('已提交')
        # return redirect(url_for('admin.pages'))
    # return render_template('admin/admin_post.html',form=form,mkds = mkds)

@site.route('/post_out')
def post_out():
    return redirect(url_for('index.index'))
    # session.pop('post_in', None)
    # return redirect(url_for('admin.pages'))

@site.route('/<type>')
def types(type):
    return redirect(url_for('index.index'))
    # admin_type = type
    # mkds = MarkDown.query.all()
    # return render_template('admin/admin_user.html',
                           # mkds = mkds,
                           # admin_type = admin_type)

