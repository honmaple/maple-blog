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
from maple import db, redis_data
from maple.blog.forms import CommentForm, ReplyForm
from maple.blog.models import Articles, Tags, Comments, Replies
from maple.main.permissions import writer_permission
from datetime import datetime

site = Blueprint('blog', __name__)


def count_sum(count):
    '''文章总数'''
    if count % 6 == 0:
        count = int(count / 6)
    else:
        count = int(count / 6) + 1
    return count


@site.route('', defaults={'number': 1})
@site.route('/page?=<int:number>')
def index_num(number):
    aa = dict(tag='a', number='1')
    a = url_for('blog.index_num',**aa)
    print(a)
    '''每页显示6篇,且按照时间排序 '''
    articles = Articles.query.offset((number - 1) * 6).limit(6)
    all_tags = Tags.query.distinct(Tags.name).all()
    count = Articles.query.count()
    count = count_sum(count)
    number = number
    return render_template('blog/blog.html',
                           title=u'HonMaple的个人博客',
                           articles=articles,
                           all_tags=all_tags,
                           count=count,
                           number=number)


@site.route('/<category>', defaults={'number': 1})
@site.route('/<category>/page?=<int:number>')
def category_num(category, number):
    all_article = Articles.load_by_category(category)
    if all_article is None:
        abort(404)
    articles = Articles.query.filter_by(category=category).offset(
        (number - 1) * 6).limit(6)
    all_tags = Tags.query.distinct(Tags.name).all()
    count = len(all_article)
    count = count_sum(count)
    number = number
    category = category
    return render_template('blog/blog_category.html',
                           title='%s - HonMaple博客' % (category),
                           articles=articles,
                           all_tags=all_tags,
                           count=count,
                           number=number,
                           category=category)


@site.route('/tag=<tag>', defaults={'number': 1})
@site.route('/tag=<tag>/page?=<int:number>')
def tag_num(tag, number):
    a = Articles.query.join(Articles.tags).filter(Tags.name == tag)
    articles = a.offset((number - 1) * 6).limit(6)
    all_tags = Tags.query.distinct(Tags.name).all()
    count = a.count()
    count = count_sum(count)
    number = number
    tag = tag
    return render_template('blog/blog_tag.html',
                           title='%s - HonMaple博客' % (tag),
                           articles=articles,
                           number=number,
                           count=count,
                           tag=tag,
                           all_tags=all_tags)


@site.route('/view/<id>')
def view(id):
    '''记录用户浏览次数'''
    redis_data.zincrby('visited:article', 'article:%s' % str(id), 1)
    comment_form = CommentForm()
    reply_form = ReplyForm()
    article = Articles.load_by_id(id)
    all_tags = Tags.query.distinct(Tags.name).all()
    tags = article.tags
    title = article.title
    return render_template('blog/blog_page.html',
                           title='%s - HonMaple博客' % (title),
                           article=article,
                           all_tags=all_tags,
                           tags=tags,
                           comment_form=comment_form,
                           reply_form=reply_form)


@site.route('/archives', defaults={'number': 1})
@site.route('/archives/page?=<int:number>')
def archives(number):
    articles = Articles.query.offset((number - 1) * 30).limit(30)
    all_tags = Tags.query.distinct(Tags.name).all()
    count = Articles.query.count()
    if count % 30 == 0:
        count = int(count / 30)
    else:
        count = int(count / 30) + 1
    number = number
    return render_template('blog/blog_archives.html',
                           title='Archives - HonMaple博客',
                           articles=articles,
                           all_tags=all_tags,
                           count=count,
                           number=number)


@site.route('/pages/preview')
def preview():
    from misaka import Markdown, HtmlRenderer
    content = request.args.get('content')
    html = HtmlRenderer()
    markdown = Markdown(html)
    return Markup(markdown(content))


@site.route('/pages/<id>/comment', methods=['GET', 'POST'])
@login_required
def comment(id):
    '''评论表单'''
    if not writer_permission.can():
        flash('你尚未验证账户')
        return redirect(url_for('blog.index_num'))
    form = CommentForm()
    if form.validate_on_submit() and request.method == "POST":
        post_comment = Comments(author=current_user.name,
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
        flash('你尚未验证账户')
        return redirect(url_for('blog.index_num'))
    form = ReplyForm()
    if form.validate_on_submit() and request.method == "POST":
        post_reply = Replies(author=current_user.name, content=form.reply.data)
        post_reply.comments_id = comment_id
        post_reply.publish = datetime.now()
        db.session.add(post_reply)
        db.session.commit()
        return redirect(url_for('blog.view', id=id, _anchor='comment'))
    return redirect(url_for('blog.view', id=id, _anchor='comment'))
