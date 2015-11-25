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
#from flask_flatpages import FlatPages
from app import register_pages

site = Blueprint('blog',__name__,url_prefix='/blog')

flatpages = register_pages()


def len_index():
    pages = (p for p in flatpages)
    return int(len(list(pages))/6) + 1

def len_type(type):
    pages = (p for p in flatpages if p['Category'] == type)
    return int(len(list(pages))/6) + 1

def len_tag(tag):
    pages = (p for p in flatpages for t in p['Tags'] if t == tag)
    return int(len(list(pages))/6) + 1

@site.route('/')
def index():
    number = 1
    num = number
    len_page = len_index()
    pages = (p for p in flatpages)
    pages = (p for i,p in enumerate(pages) if i <= number*5 and i >= number*5-5 )
    pages = (p for p in pages if 'Date' in p.meta)
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['Date'])
    return render_template('blog/blog.html',
                           pages=latest,
                           num = num,
                           len_page = len_page)

@site.route('/<int:number>')
def index_num(number):
    num = number
    len_page = len_index()
    pages = (p for p in flatpages)
    pages = (p for i,p in enumerate(pages) if i <= number*5 and i >= number*5-5 )
    pages = (p for p in pages if 'Date' in p.meta)
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['Date'])
    return render_template('blog/blog.html',
                           pages=latest,
                           num = num,
                           len_page = len_page)

@site.route('/pages/<path:path>/')
def page(path):
    page = flatpages.get_or_404(path)
    return render_template('blog/page.html', page=page)

@site.route('/type?=<type>')
def type(type):
    number = 1
    num = number
    blog_type = type
    len_page = len_type(type)
    pages = (p for p in flatpages if p['Category'] == type)
    pages = (p for i,p in enumerate(pages) if i <= number*5 and i >= number*5-5 )
    pages = (p for p in pages if 'Date' in p.meta)
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['Date'])
    return render_template('blog/blog_type.html',
                           pages = latest,
                           num = num,
                           blog_type = blog_type,
                           len_page = len_page)

@site.route('/type?=<type>/<int:number>')
def type_num(type,number):
    num = number
    blog_type = type
    len_page = len_type(type)
    pages = (p for p in flatpages if p['Category'] == type)
    pages = (p for i,p in enumerate(pages) if i <= number*5 and i >= number*5-5 )
    pages = (p for p in pages if 'Date' in p.meta)
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['Date'])
    return render_template('blog/blog_type.html',
                           pages = latest,
                           num = num,
                           blog_type = blog_type,
                           len_page = len_page)

@site.route('/tag?=<tag>')
def tag(tag):
    number = 1
    num = number
    len_page = len_tag(tag)
    blog_tag = tag
    pages = (p for p in flatpages for t in p['Tags'] if t == tag)
    pages = (p for i,p in enumerate(pages) if i <= number*5 and i >= number*5-5 )
    pages = (p for p in pages if 'Date' in p.meta)
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['Date'])
    return render_template('blog/blog_tag.html',
                           pages = latest,
                           num = num,
                           blog_tag = blog_tag,
                           len_page =len_page)

@site.route('/tag?=<tag>/<int:number>')
def tag_num(tag,number):
    num = number
    len_page = len_tag(tag)
    blog_tag = tag
    pages = (p for p in flatpages for t in p['Tags'] if t == tag)
    pages = (p for i,p in enumerate(pages) if i <= number*5 and i >= number*5-5 )
    pages = (p for p in pages if 'Date' in p.meta)
    latest = sorted(pages, reverse=True,
                    key=lambda p: p.meta['Date'])
    return render_template('blog/blog_tag.html',
                           pages = latest,
                           num = num,
                           blog_tag = blog_tag,
                           len_page =len_page)
