#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: index.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 02:21:04
# *************************************************************************
from flask import (Blueprint, render_template, request, g, url_for, redirect)
from flask_login import login_required
from maple import cache
from maple.user.models import User
from maple.blog.models import Articles
from maple.question.models import Questions
from maple.admin.models import Notices
# from maple.blog.forms import SearchForm

site = Blueprint('index', __name__)


@site.route('/')
@site.route('/index')
@cache.cached(timeout=180)
def index():
    articles = Articles.query.limit(7)
    questions = Questions.query.filter_by(private=False).limit(7)
    notice = Notices.query.first()
    return render_template('index/index.html',
                           articles=articles,
                           questions=questions,
                           notice=notice)


@site.route('/about')
@cache.cached(timeout=180)
def about():
    return render_template('index/about_me.html')


@site.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if g.search_form.validate_on_submit() and request.method == "POST":
        search = g.search_form.search.data
        return redirect(url_for('index.search_result', query=search))
    else:
        return redirect(url_for('index.index'))

# @site.route('/search/<query>', methods=['GET'])
# @login_required
# def search_result(query):
#     results = Articles.query.search(query, sort=True).all()
#     return render_template('index/search.html', results=results)
