#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: views.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 17:46:41
# *************************************************************************
from flask import (render_template, flash, redirect, url_for, request)
from flask.views import MethodView
from flask_login import current_user, login_required
from maple.extensions import cache
from maple.main.permissions import writer_permission
from maple.question.forms import QuestionForm
from maple.question.models import Question, db
from flask_maple.form import flash_errors
from flask_babelex import gettext as _


class QueListView(MethodView):
    def __init__(self):
        super(MethodView, self).__init__()
        self.form = QuestionForm()

    @cache.cached(timeout=180)
    def get(self):
        page = request.args.get('page', 1, type=int)
        filter_dict = {}
        filter_dict.update(dict(is_private=False))
        questions = Question.get_list(page, 18, filter_dict)
        data = {
            'title': _('Answer-HonMaple'),
            'questions': questions,
            'form': self.form
        }
        return render_template('question/questionlist.html', **data)

    @login_required
    def post(self):
        if not writer_permission.can():
            flash(_('You have not confirm your account'))
            return redirect(url_for('question.quelist'))
        if self.form.validate_on_submit():
            question = Question()
            question.author = current_user
            question.title = self.form.title.data
            question.describ = self.form.describ.data
            question.answer = self.form.answer.data
            '''简单私人日记实现'''
            question.is_private = self.form.private.data
            db.session.add(question)
            db.session.commit()
            flash('感谢你的提交')
            return redirect(url_for('question.quelist'))
        else:
            if self.form.errors:
                flash_errors(self.form)
            return redirect(url_for('question.quelist'))


class QuePrivateView(MethodView):
    def __init__(self):
        super(MethodView, self).__init__()
        self.form = QuestionForm()

    @login_required
    def get(self):
        page = request.args.get('page', 1, type=int)
        filter_dict = {}
        filter_dict.update(dict(is_private=True, author__id=current_user.id))
        questions = Question.get_list(page, 18, filter_dict)
        data = {
            'title': _('Answer - HonMaple'),
            'form': self.form,
            'questions': questions
        }
        return render_template('question/questionlist.html', **data)


class QueView(MethodView):
    @login_required
    def get(self, queId):
        question = Question.get(queId)
        if question.is_private and current_user.id != question.author.id:
            flash('你没有权限查看')
            return redirect(url_for('question.quelist'))
        data = {
            'title': _('%(title)s - Answer - HonMaple', title=question.title),
            'question': question
        }
        return render_template('question/question.html', **data)
