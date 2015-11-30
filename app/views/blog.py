#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint,request,\
    redirect,url_for
#from flask_flatpages import FlatPages
from flask.ext.login import current_user
from app import register_pages
from ..forms import CommentForm
from ..models import Commentdb,db

site = Blueprint('blog',__name__,url_prefix='/blog')

flatpages = register_pages()
def latest_article(pages):
    pages = (p for p in pages if 'Date' in p.meta)
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['Date'])
    return latest

def tags_list():
    pages = (p for p in flatpages)
    li = []
    for p in pages:
        for i in p['Tags']:
            li.append(i)
    lis = list(set(li))
    return lis

def len_index():
    pages = (p for p in flatpages)
    return int(len(list(pages))/6) + 1

def len_type(type):
    pages = (p for p in flatpages if p['Category'] == type)
    return int(len(list(pages))/6) + 1

def len_tag(tag):
    pages = (p for p in flatpages for t in p['Tags'] if t == tag)
    return int(len(list(pages))/6) + 1


@site.route('/latest',defaults={'number':1})
@site.route('/latest/view?=<int:number>')
def index_num(number):
    num = number
    len_page = len_index()
    tag_list = tags_list()
    pages = (p for p in flatpages)
    latest = latest_article(pages)
    latest = latest[(num-1)*6:(num-1)*6+6]
    return render_template('blog/blog.html',
                           pages=latest,
                           tag_list = tag_list,
                           num = num,
                           len_page = len_page)


@site.route('/type?=<type>',defaults={'number':1})
@site.route('/type?=<type>/view?=<int:number>')
def type_num(type,number):
    num = number
    blog_type = type
    len_page = len_type(type)
    tag_list = tags_list()
    pages = (p for p in flatpages if p['Category'] == type)
    latest = latest_article(pages)
    latest = latest[(num-1)*6:(num-1)*6+6]
    return render_template('blog/blog_type.html',
                           pages = latest,
                           num = num,
                           tag_list = tag_list,
                           blog_type = blog_type,
                           len_page = len_page)


@site.route('/tag?=<tag>',defaults={'number':1})
@site.route('/tag?=<tag>/view?=<int:number>')
def tag_num(tag,number):
    num = number
    len_page = len_tag(tag)
    blog_tag = tag
    tag_list = tags_list()
    pages = (p for p in flatpages for t in p['Tags'] if t == tag)
    latest = latest_article(pages)
    latest = latest[(num-1)*6:(num-1)*6+6]
    return render_template('blog/blog_tag.html',
                           pages = latest,
                           num = num,
                           tag_list = tag_list,
                           blog_tag = blog_tag,
                           len_page =len_page)


@site.route('/pages/<path:path>/',methods=['GET','POST'])
def page(path):
    form = CommentForm()
    all_comment = Commentdb.query.all()
    page = flatpages.get_or_404(path)
    pages = (p for p in flatpages)
    latest = latest_article(pages)
    n = 0
    for pa in latest:
        if pa == page:
            break
        n += 1
    if n == 0:
        page_previous = None
        page_next = latest[n+1]
    elif n == len(latest) - 1:
        page_previous = latest[n-1]
        page_next = None
    else:
        page_previous = latest[n-1]
        page_next = latest[n+1]
    if request.method == 'POST':
        comments = Commentdb(name = current_user.name,
                             comment = form.comment.data)
        db.session.add(comments)
        db.session.commit()
        return redirect(url_for('blog.page',path=path))
    return render_template('blog/page.html', page = page,
                           page_previous = page_previous,
                           page_next = page_next,
                           all_comment = all_comment,
                           path = path,
                           form = form)
@site.route('/pages/<path:path>/<comment_user>?comment')
def comment(path,comment_user):
    all_comment = Commentdb.query.all()
    page = flatpages.get_or_404(path)
    form = CommentForm()
    if request.method == 'POST':
        comments = Commentdb(name = current_user.name,
                             comment = form.comment.data)
        db.session.add(comments)
        db.session.commit()
        return redirect(url_for('blog.page',path=path))
    return render_template('blog/comment.html',
                           form = form,
                           page = page,
                           all_comment = all_comment)






















