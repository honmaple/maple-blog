#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: ask.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 17:46:41
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint, \
    flash, redirect, url_for,g
from flask.ext.login import  current_user, login_required
from ..forms import ArticleForm
from ..models import Articledb,db

site = Blueprint('ask',__name__,url_prefix='/ask')


@site.before_request
def before_request():
    g.user = current_user

@site.route('/view?')
@login_required
def index():
    form = ArticleForm()
    all_questions = Articledb.query.all()
    return render_template('ask/ask.html',
                           all_questions = all_questions,
                           form = form)

@site.route('/view?post', methods=['GET','POST'])
@login_required
def ask_post():
    form = ArticleForm()
    all_questions = Articledb.query.all()
    if form.validate_on_submit():
            question = Articledb(name = current_user.name,
                                title = form.title.data,
                                describ = form.describ.data,
                                answer = form.answer.data)
            db.session.add(question)
            db.session.commit()
            flash('感谢你的提交')
            return redirect(url_for('ask.index'))
    return render_template('ask/ask.html',
                           all_questions = all_questions,
                           form = form)

@site.route('/view?question=<title>')
@login_required
def ask_question(title):
    question = Articledb.query.filter_by(title=title).first()
    return render_template('ask/question.html',
                           question = question)















