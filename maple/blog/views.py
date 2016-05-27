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
                   abort, Markup, flash)
from flask_login import current_user, login_required
from maple import db, redis_data, cache
from maple.blog.forms import CommentForm, ReplyForm
from maple.blog.models import Articles, Tags, Comments, Replies
from maple.main.permissions import writer_permission
from maple.main.helpers import is_num
from datetime import datetime
from flask_babel import gettext as _
from urllib.parse import urljoin
from werkzeug.contrib.atom import AtomFeed

site = Blueprint('blog', __name__)


def make_external(url):
    return urljoin(request.url_root, url)


@site.route('')
@cache.cached(timeout=180)
def index_num():
    '''每页显示6篇,且按照时间排序 '''
    page = is_num(request.args.get('page'))
    articles = Articles.query.paginate(page, 6, True)
    all_tags = Tags.query.distinct(Tags.name).all()
    return render_template('blog/blog.html',
                           articles=articles,
                           all_tags=all_tags)


@site.route('/<category>')
@cache.cached(timeout=180)
def category_num(category):
    all_article = Articles.load_by_category(category)
    if all_article is None:
        abort(404)
    page = is_num(request.args.get('page'))
    articles = Articles.query.filter_by(category=category).paginate(page, 6,
                                                                    True)
    all_tags = Tags.query.distinct(Tags.name).all()
    category = category
    return render_template('blog/blog_category.html',
                           articles=articles,
                           all_tags=all_tags,
                           category=category)


@site.route('/tag=<tag>')
@cache.cached(timeout=180)
def tag_num(tag):
    page = is_num(request.args.get('page'))
    articles = Articles.query.join(Articles.tags).filter(
        Tags.name == tag).paginate(page, 6, True)
    all_tags = Tags.query.distinct(Tags.name).all()
    tag = tag
    return render_template('blog/blog_tag.html',
                           articles=articles,
                           tag=tag,
                           all_tags=all_tags)


@site.route('/view/<int:id>')
@cache.cached(timeout=180)
def view(id):
    '''记录用户浏览次数'''
    redis_data.zincrby('visited:article', 'article:%s' % str(id), 1)
    comment_form = CommentForm()
    reply_form = ReplyForm()
    article = Articles.load_by_id(id)
    all_tags = Tags.query.distinct(Tags.name).all()
    tags = article.tags
    return render_template('blog/blog_page.html',
                           article=article,
                           all_tags=all_tags,
                           tags=tags,
                           comment_form=comment_form,
                           reply_form=reply_form)


@site.route('/archives')
@cache.cached(timeout=180)
def archives():
    page = is_num(request.args.get('page'))
    articles = Articles.query.paginate(page, 30, True)
    all_tags = Tags.query.distinct(Tags.name).all()
    return render_template('blog/blog_archives.html',
                           articles=articles,
                           all_tags=all_tags)


@site.route('/atom.xml')
def feed():
    feed = AtomFeed('Recent Articles',
                    feed_url=request.url,
                    url=request.url_root,
                    subtitle='I like solitude, yearning for freedom')
    articles = Articles.query.limit(15).all()
    for article in articles:
        feed.add(
            article.title,
            article.content,
            content_type='html',
            author=article.author,
            url=make_external(url_for('blog.view', id=article.id)),
            updated=article.publish,
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


@site.route('/pages/<id>/<comment_id>', methods=['GET', 'POST'])
@login_required
def reply(id, comment_id):
    '''回复表单'''
    if not writer_permission.can():
        flash(_('You have not confirm your account'))
        return redirect(url_for('blog.index_num'))
    form = ReplyForm()
    if form.validate_on_submit() and request.method == "POST":
        post_reply = Replies(author=current_user.username,
                             content=form.reply.data)
        post_reply.comments_id = comment_id
        post_reply.publish = datetime.now()
        db.session.add(post_reply)
        db.session.commit()
        return redirect(url_for('blog.view', id=id, _anchor='comment'))
    return redirect(url_for('blog.view', id=id, _anchor='comment'))
