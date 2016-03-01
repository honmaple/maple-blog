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
    redirect,url_for,abort,Markup
from flask.ext.login import current_user,login_required
from ..forms import CommentForm,ReplyForm
from ..models import Comments,db,Replies,Articles,Tags
from ..utils import writer_permission
from datetime import datetime
from app import redis_data

# site = Blueprint('blog',__name__,url_prefix='/blog')
site = Blueprint('blog',__name__,url_prefix='/blog')

def count_sum(count):
    '''文章总数'''
    if count%6 == 0:
        count = int(count/6)
    else:
        count = int(count/6) + 1
    return count

@site.route('/latest',defaults={'number':1})
@site.route('/latest/view?=<int:number>')
def index_num(number):
    '''每页显示6篇,且按照时间排序 '''
    articles = Articles.query.order_by(Articles.publish.desc()).\
        offset((number-1)*6).limit(6)
    all_tags = Tags.query.distinct(Tags.name).all()
    count = Articles.query.count()
    count = count_sum(count)
    number = number
    return render_template('blog/blog.html',
                        title = u'HonMaple的个人博客',
                        articles = articles,
                        all_tags = all_tags,
                        count = count,
                        number = number)


@site.route('/category=<category>',defaults={'number':1})
@site.route('/category=<category>/view?=<int:number>')
def category_num(category,number):
    if category != 'linux' and category != 'python' and category != '生活随笔':
        abort(404)
    articles = Articles.query.order_by(Articles.publish.desc()).\
        filter_by(category=category).\
        offset((number-1)*6).limit(6)
    all_tags = Tags.query.distinct(Tags.name).all()
    count = Articles.query.filter_by(category=category).count()
    count = count_sum(count)
    number = number
    category = category
    return render_template('blog/blog_category.html',
                           title = '%s - HonMaple博客'%(category),
                           articles = articles,
                           all_tags = all_tags,
                           count = count,
                           number = number,
                           category = category)


@site.route('/tag=<tag>',defaults={'number':1})
@site.route('/tag=<tag>/view?=<int:number>')
def tag_num(tag,number):
    tags = Tags.query.filter_by(name=tag).\
        offset((number-1)*6).limit(6)
    if tags.count() == 0:
        abort(404)
    all_tags = Tags.query.distinct(Tags.name).all()
    count = Tags.query.filter_by(name=tag).count()
    count = count_sum(count)
    number = number
    tag = tag
    return render_template('blog/blog_tag.html',
                           title = '%s - HonMaple博客'%(tag),
                           tags = tags,
                           number = number,
                           count = count,
                           tag = tag,
                           all_tags = all_tags)

@site.route('/pages/<id>')
def page(id):
    '''记录用户浏览次数'''
    redis_data.zincrby('visited:article','article:%s'%str(id),1)
    comment_form = CommentForm()
    reply_form = ReplyForm()
    article = Articles.query.filter_by(id=id).first()
    all_tags = Tags.query.distinct(Tags.name).all()
    tags = article.tag_article
    title = article.title
    return render_template('blog/blog_page.html',
                           title = '%s - HonMaple博客'%(title),
                           article = article,
                           all_tags = all_tags,
                           tags = tags,
                           comment_form = comment_form,
                           reply_form = reply_form)

@site.route('/archives',defaults={'number':1})
@site.route('/archives/view?=<int:number>')
def archives(number):
    articles = Articles.query.order_by(Articles.publish.desc()).\
        offset((number-1)*30).limit(30)
    all_tags = Tags.query.distinct(Tags.name).all()
    count = Articles.query.count()
    if count%30 == 0:
        count = int(count/30)
    else:
        count = int(count/30) + 1
    number = number
    return render_template('blog/blog_archives.html',
                           title = 'Archives - HonMaple博客',
                           articles = articles,
                           all_tags = all_tags,
                           count = count,
                           number = number)

@site.route('/pages/preview')
def preview():
    from misaka import Markdown, HtmlRenderer
    content = request.args.get('content')
    html = HtmlRenderer()
    markdown = Markdown(html)
    return Markup(markdown(content))

'''评论表单'''
@site.route('/pages/<id>/comment',methods=['GET','POST'])
@login_required
@writer_permission.require(404)
def comment(id):
    form = CommentForm()
    if form.validate_on_submit() and request.method == "POST":
        post_comment = Comments(user = current_user.name,
                                content = form.comment.data)
        post_comment.articles_id = id
        post_comment.publish = datetime.now()
        db.session.add(post_comment)
        db.session.commit()
        return redirect(url_for('blog.page',id=id,_anchor='comment'))
    return redirect(url_for('blog.page',id=id,_anchor='comment'))

'''回复表单'''
@site.route('/pages/<id>/<comment_id>',methods=['GET','POST'])
@login_required
@writer_permission.require(404)
def reply(id,comment_id):
    form = ReplyForm()
    if form.validate_on_submit() and request.method == "POST":
        post_reply = Replies( user = current_user.name,
                             content = form.reply.data)
        post_reply.comments_id = comment_id
        post_reply.publish = datetime.now()
        db.session.add(post_reply)
        db.session.commit()
        return redirect(url_for('blog.page',id=id,_anchor='comment'))
    return redirect(url_for('blog.page',id=id,_anchor='comment'))
