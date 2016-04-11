#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint
from ..models import Books


site = Blueprint('book',__name__,url_prefix='/book')


@site.route('/latest',defaults={'num':1})
@site.route('/latest/view?=<int:num>')
def index_num(num):
    book_all_type = Books.query.distinct(Books.tag)
    books = Books.query.distinct(Books.name).all()
    total = int(len(books)/18) + 1
    number = num
    add = number - 1
    if num == add + 6:
        add += 5
    return render_template('book/book.html',
                           books = books,
                           book_all_type = book_all_type,
                           add = add,
                           number = number,
                           total = total)

@site.route('/type?=<type>')
def type(type):
    book_all_type = Books.query.distinct(Books.tag)
    books = Books.query.distinct(Books.name).filter_by(tag=type)
    return render_template('book/book_type.html',
                           books = books,
                           book_all_type = book_all_type)

@site.route('/name=<name>')
def book_intro(name):
    books = Books.query.filter_by(name=name).first()
    return render_template('book/book_intro.html',
                           books = books)



