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
from flask.views import MethodView
from flask_login import current_user, login_required
from maple import cache
from maple.question.forms import QuestionForm
from maple.question.models import Question, db
from flask_maple.forms import flash_errors
from flask_babelex import gettext as _
from datetime import datetime


class QueListView(MethodView):
    def __init__(self):
        super(MethodView, self).__init__()
        self.form = QuestionForm()

    def get(self):
        page = request.args.get('page', 1, type=int)
        filter_dict = {}
        filter_dict.update(is_private=False)
        questions = Question.get_question_list(page, filter_dict)
        data = {
            'title': _('自问自答-HonMaple'),
            'questions': questions,
            'form': self.form
        }
        return render_template('question/questionlist.html', **data)

    def post(self):
        if self.form.validate_on_submit():
            post_question = Question(
                author=current_user.username,
                title=self.form.title.data,
                describ=self.form.describ.data,
                answer=self.form.answer.data)
            '''简单私人日记实现'''
            post_question.publish = datetime.now()
            post_question.private = self.form.private.data
            db.session.add(post_question)
            db.session.commit()
            flash('感谢你的提交')
            return redirect(url_for('question.quelist'))
        else:
            if self.form.errors:
                flash_errors(self.form)
            return redirect(url_for('question.quelist'))


class QuePrivateView(MethodView):
    def get(self):
        page = request.args.get('page', 1, type=int)
        filter_dict = {}
        filter_dict.update(is_private=True)
        questions = Question.get_question_list(page, filter_dict)
        data = {'title': _('自问自答 - HonMaple'), 'questions': questions}
        return render_template('question/questionlist.html', **data)


class QueView(MethodView):
    def get(self, queId):
        question = Question.get(queId)
        if question.is_private and current_user != question.author:
            flash('你没有权限查看')
            return redirect(url_for('question.quelist'))
        data = {
            'title': _('%(title)s - 自问自答 - HonMaple', title=question.title),
            'question': question
        }
        return render_template('question/question.html', **data)
