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
from flask_login import login_required
from maple.extensions import cache
from maple.main.permissions import writer_permission
from maple.question.forms import QuestionForm
from maple.question.models import Question
from flask_maple.form import flash_errors
from flask_babelex import gettext as _
from maple.common.views import BaseMethodView as MethodView
from maple.common.utils import (gen_filter_dict, gen_order_by)


class QueListView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        query_dict = request.data
        page, number = self.page_info
        keys = ['title']
        equal_key = []
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key)
        filter_dict.update(dict(is_private=False))
        questions = Question.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        data = {
            'title': _('Answer-HonMaple'),
            'questions': questions,
            'form': QuestionForm()
        }
        return render_template('question/questionlist.html', **data)

    @login_required
    def post(self):
        form = QuestionForm()
        user = request.user
        if not writer_permission.can():
            flash(_('You have not confirm your account'))
            return redirect(url_for('question.quelist'))
        if form.validate_on_submit():
            question = Question()
            question.author = user
            question.title = form.title.data
            question.describ = form.describ.data
            question.answer = form.answer.data
            '''简单私人日记实现'''
            question.is_private = form.private.data
            question.save()
            flash('感谢你的提交')
            return redirect(url_for('question.quelist'))
        else:
            if form.errors:
                flash_errors(form)
            return redirect(url_for('question.quelist'))


class QuePrivateView(MethodView):
    @login_required
    def get(self):
        query_dict = request.data
        user = request.user
        page, number = self.page_info
        keys = ['title']
        equal_key = []
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys, equal_key, user)
        filter_dict.update(dict(is_private=True))
        questions = Question.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number)
        data = {
            'title': _('Answer - HonMaple'),
            'form': QuestionForm(),
            'questions': questions
        }
        return render_template('question/questionlist.html', **data)


class QueView(MethodView):
    @login_required
    def get(self, queId):
        user = request.user
        question = Question.query.filter_by(id=queId).first_or_404()
        if question.is_private and user.id != question.author.id:
            flash('你没有权限查看')
            return redirect(url_for('question.quelist'))
        data = {
            'title': _('%(title)s - Answer - HonMaple', title=question.title),
            'question': question
        }
        return render_template('question/question.html', **data)
