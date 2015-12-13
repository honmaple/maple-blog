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
    redirect,url_for,g,Markup
from flask.ext.login import current_user,login_required
import markdown
from ..forms import CommentForm
from ..models import Comments,db,Replies,Articles,Tags,Category

site = Blueprint('blog',__name__,url_prefix='/blog')


@site.before_request
def before_request():
    g.user = current_user

@site.route('/latest',defaults={'number':1})
@site.route('/latest/view?=<int:number>')
def index_num(number):
    articles = Articles.query.order_by(Articles.publish).\
        offset((number-1)*9).limit(number*9)
    all_tags = Tags.query.all()
    count = Articles.query.count()
    count = int(count/9) + 1
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
    categories = Category.query.filter_by(name=category).first()
    all_tags = Tags.query.all()
    articles = categories.articles
    count = articles.count()
    count = int(count/9) + 1
    number = number
    category = category
    return render_template('blog/blog_category.html',
                           title = '%s -HonMaple博客'%(category),
                           articles = articles,
                           all_tags = all_tags,
                           count = count,
                           number = number,
                           category = category)


@site.route('/tag=<tag>',defaults={'number':1})
@site.route('/tag=<tag>/view?=<int:number>')
def tag_num(tag,number):
    tags = Tags.query.filter_by(name=tag).first()
    all_tags = Tags.query.all()
    articles = tags.tag_article
    count = len(articles)
    count = int(count/9) + 1
    number = number
    tag = tag
    return render_template('blog/blog_tag.html',
                           title = '%s -HonMaple博客'%(tag),
                           articles = articles,
                           number = number,
                           count = count,
                           tag = tag,
                           all_tags = all_tags)

@site.route('/pages/<title>')
def page(title):
    form = CommentForm()
    article = Articles.query.filter_by(title=title).first()
    tags = article.tag_article
    content = Markup(markdown.markdown(article.content))
    all_comment = Comments.query.filter_by(page_title=title).all()
    return render_template('blog/blog_page.html',
                           title = '%s -HonMaple博客'%(title),
                           article = article,
                           content = content,
                           tags = tags,
                           all_comment = all_comment,
                           form = form)
'''评论表单'''
@site.route('/pages/<title>/comment',methods=['GET','POST'])
@login_required
def comment(title):
    form = CommentForm()
    article = Articles.query.filter_by(title=title).first()
    if request.method == 'POST':
        post_comment = Comments(comment_user = current_user.name,
                                comment_content = form.comment.data,
                                page_title = article.title)
        db.session.add(post_comment)
        db.session.commit()
        return redirect(url_for('blog.page',title=title,_anchor='comment'))
    return redirect(url_for('blog.page',title=title,_anchor='comment'))

'''回复表单'''
@site.route('/pages/<title>/<comment_id>',methods=['GET','POST'])
@login_required
def reply(title,comment_id):
    form = CommentForm()
    if request.method == 'POST':
        post_reply = Replies( reply_user = current_user.name,
                             reply_content = form.reply.data,
                             comments_id = comment_id)
        db.session.add(post_reply)
        db.session.commit()
        return redirect(url_for('blog.page',title=title,_anchor='comment'))
    return redirect(url_for('blog.page',title=title,_anchor='comment'))







