#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: views.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 17:46:41
# *************************************************************************
from flask import (render_template, Blueprint, flash, redirect, url_for,
                   request)
from flask_login import current_user, login_required
from maple import cache
from maple.question.forms import QuestionForm
from maple.question.models import Questions, db
from maple.forms.forms import flash_errors
from datetime import datetime

site = Blueprint('question', __name__)


@site.route('')
@cache.cached(timeout=180)
def index():
    form = QuestionForm()
    questions = Questions.query.filter_by(private=False).all()
    return render_template('question/question.html',
                           title='自问自答-HonMaple',
                           questions=questions,
                           form=form)


@site.route('/view', methods=['GET', 'POST'])
@login_required
@cache.cached(timeout=180)
def post():
    form = QuestionForm()
    if form.validate_on_submit() and request.method == "POST":
        post_question = Questions(author=current_user.username,
                                  title=form.title.data,
                                  describ=form.describ.data,
                                  answer=form.answer.data)
        '''简单私人日记实现'''
        post_question.publish = datetime.now()
        post_question.private = form.private.data
        db.session.add(post_question)
        db.session.commit()
        flash('感谢你的提交')
        return redirect(url_for('question.index'))
    else:
        if form.errors:
            flash_errors(form)
        else:
            pass
        return redirect(url_for('question.index'))


@site.route('/private')
@login_required
@cache.cached(timeout=180)
def private():
    form = QuestionForm()
    questions = Questions.load_by_private()
    return render_template('question/question.html',
                           questions=questions,
                           title='自问自答-HonMaple',
                           form=form)


@site.route('/view?=<id>')
@login_required
@cache.cached(timeout=180)
def question_view(id):
    question = Questions.load_by_id(id)
    if question.private and current_user.username != question.author:
        flash('你没有权限查看')
        return redirect(url_for('question.index'))
    return render_template('question/question_view.html',
                           title='%s - HonMaple自问自答' % (question.title),
                           question=question)
