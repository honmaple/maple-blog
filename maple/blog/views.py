#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
# *************************************************************************
from flask import (render_template, Blueprint, request, redirect, url_for,
                   flash)
from flask_login import current_user, login_required
from maple import db, redis_data, cache
from maple.blog.forms import CommentForm
from maple.blog.models import Articles, Tags, Comments
from maple.main.permissions import writer_permission
from maple.main.helpers import is_num
from datetime import datetime
from flask_babelex import gettext as _
from urllib.parse import urljoin
from maple.filters import safe_markdown
from sqlalchemy import func
from werkzeug.contrib.atom import AtomFeed
from werkzeug.utils import escape

site = Blueprint('blog', __name__)


def make_external(url):
    return urljoin(request.url_root, url)


@site.route('')
@cache.cached(timeout=180)
def index():
    '''每页显示6篇,且按照时间排序 '''
    page = is_num(request.args.get('page'))
    articles = Articles.query.paginate(page, 6, True)
    return render_template('blog/blog.html', articles=articles)


@site.route('/<category>')
@cache.cached(timeout=180)
def category(category):
    page = is_num(request.args.get('page'))
    articles = Articles.query.filter(func.lower(
        Articles.category) == func.lower(category)).paginate(page, 6, True)
    return render_template('blog/blog_category.html',
                           articles=articles,
                           category=category)


@site.route('/tag=<tag>')
@cache.cached(timeout=180)
def tag(tag):
    page = is_num(request.args.get('page'))
    articles = Articles.query.join(Articles.tags).filter(func.lower(
        Tags.name) == func.lower(tag)).paginate(page, 6, True)
    return render_template('blog/blog_tag.html', articles=articles, tag=tag)


@site.route('/view/<int:id>')
@cache.cached(timeout=180)
def view(id):
    '''记录用户浏览次数'''
    redis_data.zincrby('visited:article', 'article:%s' % str(id), 1)
    comment_form = CommentForm()
    article = Articles.load_by_id(id)
    tags = article.tags
    return render_template('blog/blog_page.html',
                           article=article,
                           tags=tags,
                           comment_form=comment_form)


@site.route('/archives')
@cache.cached(timeout=180)
def archives():
    page = is_num(request.args.get('page'))
    articles = Articles.query.paginate(page, 30, True)
    return render_template('blog/blog_archives.html', articles=articles)


@site.route('/atom.xml')
def feed():
    feed = AtomFeed('HoMaple的个人博客',
                    feed_url=request.url,
                    url=request.url_root,
                    subtitle='I like solitude, yearning for freedom')
    articles = Articles.query.limit(15).all()
    for article in articles:
        feed.add(article.title,
                 escape(safe_markdown(article.content)),
                 content_type='html',
                 author=article.author,
                 url=make_external(url_for('blog.view',
                                           id=article.id)),
                 updated=article.updated
                 if article.updated is not None else article.publish,
                 published=article.publish)
    return feed.get_response()


@site.route('/pages/<id>/comment', methods=['GET', 'POST'])
@login_required
def comment(id):
    '''评论表单'''
    if not writer_permission.can():
        flash(_('You have not confirm your account'))
        return redirect(url_for('blog.index_num'))
    form = CommentForm()
    if form.validate_on_submit() and request.method == "POST":
        post_comment = Comments(author=current_user.username,
                                content=form.comment.data)
        post_comment.articles_id = id
        post_comment.publish = datetime.now()
        db.session.add(post_comment)
        db.session.commit()
        return redirect(url_for('blog.view', id=id, _anchor='comment'))
    return redirect(url_for('blog.view', id=id, _anchor='comment'))
