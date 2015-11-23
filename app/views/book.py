#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint, url_for, \
    request
from ..models import Books


site = Blueprint('book',__name__,url_prefix='/book')

@site.route('/')
def index():
    books = Books.query.all()
    number = 1
    add = 0
    total = int(len(books)/15) + 1
    return render_template('book/book.html',
                           books = books,
                           add = add,
                           number = number,
                           total = total)

@site.route('/page=<int:num>',methods=['GET','POST'])
def index_num(num):
    books = Books.query.all()
    total = int(len(books)/15) + 1
    number = num
    add = number - 1
    if num == add + 6:
        add += 5
    return render_template('book/book.html',
                           books = books,
                           add = add,
                           number = number,
                           total = total)

@site.route('/name=<name>')
def book_intro(name):
    books = Books.query.filter_by(name=name).first()
    return render_template('book/book_intro.html',
                           books = books)



