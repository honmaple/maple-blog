#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: question.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 17:46:41
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint, \
    flash, redirect, url_for,g,request
from flask.ext.login import  current_user, login_required
from ..forms import QuestionForm
from ..models import Questions,db

site = Blueprint('question',__name__,url_prefix='/question')


@site.before_request
def before_request():
    g.user = current_user

@site.route('/view')
@login_required
def index():
    form = QuestionForm()
    all_questions = Questions.query.all()
    return render_template('question/question.html',
                           all_questions = all_questions,
                           form = form)

@site.route('/view?post', methods=['GET','POST'])
@login_required
def question_post():
    form = QuestionForm()
    all_questions = Questions.query.all()
    if request.method == "POST":
        post_question = Questions(user = current_user.name,
                                  title = form.title.data,
                                  describ = form.describ.data,
                                  answer = form.answer.data)
        db.session.add(post_question)
        db.session.commit()
        flash('感谢你的提交')
        return redirect(url_for('question.index'))
    return render_template('question/question.html',
                           all_questions = all_questions,
                           form = form)

@site.route('/view?question=<title>')
@login_required
def question_view(title):
    question = Questions.query.filter_by(title=title).first()
    return render_template('question/question_view.html',
                           question = question)















