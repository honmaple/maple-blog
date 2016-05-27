#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
# *************************************************************************
from flask import render_template, Blueprint, request
from maple import cache
from maple.main.helpers import is_num
from maple.books.models import Books

site = Blueprint('book', __name__)


@site.route('')
@cache.cached(timeout=300)
def index_num():
    page = is_num(request.args.get('page'))
    book_all_tags = Books.query.distinct(Books.tag)
    books = Books.query.distinct(Books.name).paginate(page, 18, True)
    return render_template('book/book.html',
                           books=books,
                           book_all_tags=book_all_tags)


@site.route('/tag?=<tag>')
@cache.cached(timeout=180)
def tag(tag):
    book_all_type = Books.query.distinct(Books.tag)
    books = Books.query.distinct(Books.name).filter_by(tag=tag)
    return render_template('book/book_type.html',
                           books=books,
                           tag=tag,
                           book_all_type=book_all_type)


@site.route('/name=<name>')
@cache.cached(timeout=180)
def book_intro(name):
    books = Books.query.filter_by(name=name).first()
    return render_template('book/book_intro.html', books=books)
