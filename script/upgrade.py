#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: upgrade.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-03-11 17:12:06 (CST)
# Last Update: Tuesday 2018-11-06 13:52:20 (CST)
#          By:
# Description:
# ********************************************************************************
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from runserver import app
from maple.extension import db, redis
from maple.model import (Blog, Tag, Category, User, TimeLine, Question,
                         tag_blog)

engine = create_engine('postgresql://postgres:password@localhost/blog_backup')
session = sessionmaker(bind=engine)()


def date(i):
    return {"created_at": i.created_at, "updated_at": i.updated_at}


def upgrade_user():
    print('upgrade user ...')
    users = session.execute('select * from users;')
    User.bulk_save([User(
        id=user.id,
        username=user.username,
        email=user.email,
        password=user.password,
        is_superuser=user.is_superuser,
        is_confirmed=user.is_confirmed) for user in users])


def upgrade_timeline():
    print('upgrade timeline ...')
    timelines = session.execute('select * from timeline;')
    Tag.bulk_save([TimeLine(
        id=i.id,
        content=i.content,
        is_hidden=i.hide,
        user_id=i.author_id,
        **date(i)) for i in timelines])


def upgrade_question():
    print('upgrade question ...')
    questions = session.execute('select * from questions;')
    Question.bulk_save([Question(
        id=i.id,
        title=i.title,
        is_hidden=i.is_private,
        answer=i.answer,
        description=i.describ,
        user_id=i.author_id,
        created_at=i.created_at) for i in questions])


def upgrade_blog():
    print('upgrade tag ...')
    tags = session.execute('select * from tags;')
    Tag.bulk_save([Tag(id=i.id, name=i.name) for i in tags])

    print('upgrade category ...')
    categories = session.execute('select * from categories;')
    Category.bulk_save([Category(id=i.id, name=i.name) for i in categories])

    print('upgrade blog ...')
    blogs = session.execute('select * from blogs;')
    Blog.bulk_save([Blog(
        id=blog.id,
        title=blog.title,
        content=blog.content,
        content_type=blog.content_type,
        is_copy=blog.is_copy,
        category_id=blog.category_id,
        user_id=blog.author_id,
        **date(blog)) for blog in blogs])

    print('upgrade tag_blog ...')
    tag_blogs = session.execute('select * from tag_blog;')
    db.engine.execute(tag_blog.insert(), [{
        'tag_id': i.tags_id,
        'blog_id': i.blogs_id
    } for i in tag_blogs])


def upgrade_setval():
    print('upgrade setval ...')
    db.engine.execute("select setval('tag_id_seq',(select max(id) from tag))")
    db.engine.execute(
        "select setval('blog_id_seq',(select max(id) from blog))")
    db.engine.execute(
        "select setval('category_id_seq',(select max(id) from category))")
    db.engine.execute(
        "select setval('timeline_id_seq',(select max(id) from timeline))")
    db.engine.execute(
        "select setval('question_id_seq',(select max(id) from question))")
    db.engine.execute(
        "select setval('user_id_seq',(select max(id) from \"user\"))")


def upgrade_redis():
    print("upgrade redis ...")
    redis.rename("visited:article", "count:article:visited")


if __name__ == '__main__':
    with app.app_context():
        upgrade_user()
        upgrade_blog()
        upgrade_timeline()
        upgrade_question()
        upgrade_setval()
        upgrade_redis()
