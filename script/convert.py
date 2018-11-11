#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: convert.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-03-10 18:37:00 (CST)
# Last Update: Tuesday 2018-11-06 13:52:20 (CST)
#          By:
# Description:
# ********************************************************************************
import os
from datetime import datetime
from re import compile

from runserver import app
from maple.model import Blog, Category, Tag, User

org_regex = {
    'title': compile(r'^#\+TITLE:(.*?)$'),
    'date': compile(r'^#\+DATE:(.*?)$'),
    'category': compile(r'^#\+CATEGORY:(.*?)$'),
    'author': compile(r'^#\+AUTHOR:(.*?)$'),
    'summary': compile(r'^#\+PROPERTY:\s+SUMMARY (.*?)$'),
    'slug': compile(r'^#\+PROPERTY:\s+SLUG (.*?)$'),
    'language': compile(r'^#\+PROPERTY:\s+LANGUAGE (.*?)$'),
    'modified': compile(r'^#\+PROPERTY:\s+MODIFIED (.*?)$'),
    'tags': compile(r'^#\+PROPERTY:\s+TAGS (.*?)$'),
    'save_as': compile(r'^#\+PROPERTY:\s+SAVE_AS (.*?)$'),
    'status': compile(r'^#\+PROPERTY:\s+STATUS (.*?)$')
}


def write_to_blog(attr, file_type='org'):
    _author = attr['author']
    _category = attr['category']
    _tags = attr['tags'].split(',')
    _title = attr['title']
    _date = attr['date']
    _content = attr['content']

    user = User.query.filter_by(username=_author).first()
    if not user:
        user = User(username=_author, email='mail@honmaple.com')
        user.set_password('123123')
        user.save()

    category = Category.query.filter_by(name=_category).first()
    if not category:
        category = Category(name=_category)
        category.save()

    tags = []
    for _tag in _tags:
        tag = Tag.query.filter_by(name=_tag).first()
        if not tag:
            tag = Tag(name=_tag)
            tag.save()
        tags.append(tag)

    try:
        _date = datetime.strptime(_date, '%Y-%m-%d'),
    except ValueError:
        _date = datetime.strptime(_date, '%Y-%m-%d %H:%M:%S'),

    blog = Blog.query.filter_by(title=_title).first()
    if not blog:
        blog = Blog(
            title=_title,
            category_id=category.id,
            content=_content,
            created_at=_date,
            tags=tags,
            content_type='1' if file_type == 'org' else '0',
            user_id=user.id)
        blog.save()

    return blog


def org_to_blog(filename):
    filename = os.path.join(page_path, 'org', filename)
    print(filename)
    with open(filename, 'r') as f:
        text = f.readlines()
    lines = text[:15]
    attr = {}
    for name, regex in org_regex.items():
        for line in lines:
            if regex.match(line):
                attr[name] = regex.match(line).group(1).strip()
                break
    for index, line in enumerate(text):
        if not line.startswith("#+"):
            break
    attr['content'] = ''.join(text[index:])
    with app.app_context():
        blog = write_to_blog(attr)
    return blog


def md_to_blog():
    pass


page_path = '/home/jianglin/git/pelican/content'

org_files = os.listdir('/home/jianglin/git/pelican/content/org')
orgs = [org_to_blog(i) for i in org_files]

print(orgs)

# md_files = os.listdir('/home/jianglin/git/pelican/content/markdown')
# mds = [md_to_blog(i) for i in md_files]

# app.run()
