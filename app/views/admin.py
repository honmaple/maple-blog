#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: blog.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 08:11:38
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint, request, \
    session, flash, redirect, url_for ,Markup
from flask.ext.login import current_user
import markdown
from ..models import Articles,db,User,Comments,Questions,Tags,Category
from ..forms import ArticleForm
from ..utils import Permission

site = Blueprint('admin',__name__,url_prefix='/admin')

@site.route('/')
@Permission('admin')
def index():
    # return redirect(url_for('index.index'))
   return render_template('admin/admin.html')

@site.route('/pages_post', methods=['GET','POST'])
def pages():
    # return redirect(url_for('index.index'))
    articles = Articles.query.all()
    form = ArticleForm()
    # asd = Category.query.filter_by(name='linux').all()
    # for i in asd:
        # for j in i.articles:
            # print(j.title)
    # h = Articles.query.filter_by(id=18).first()
    # print(h.tag_article)
    # w = Tags.query.filter_by(name='linux').all()
    # for i in w:
        # print(i.tag_article)
    if request.method == 'POST':
        '''分类节点'''
        tags = form.tags.data.split(',')
        post_tags = []
        for tag in tags:
            '''判断节点是否存在'''
            existed_tag = Tags.query.filter_by(name=tag).first()
            if existed_tag:
                t = existed_tag
            else:
                t = Tags(name = tag)
            post_tags.append(t)
        '''判断分类是否存在'''
        existed_category = Category.query.filter_by(name=\
                                                    form.category.data).first()
        if existed_category:
            post_category = existed_category
        else:
            post_category = Category(name=form.category.data)
        post_article = Articles(user = current_user.name,
                                title = form.title.data,
                                summary = form.summary.data,
                                content = form.content.data)
        '''关系数据表'''
        post_article.tag_article = post_tags
        post_article.category = post_category
        db.session.add(post_article)
        db.session.commit()
        session['post_in'] = True
        flash('已提交')
        return redirect(url_for('admin.pages'))
    return render_template('admin/admin_post.html',
                           form=form,
                           articles = articles)

@site.route('/post_out')
def post_out():
    # return redirect(url_for('index.index'))
    session.pop('post_in', None)
    return redirect(url_for('admin.pages'))

@site.route('/<type>')
def types(type):
    return redirect(url_for('index.index'))
    # admin_type = type
    # mkds = Articles.query.all()
    # return render_template('admin/admin_user.html',
                           # mkds = mkds,
                           # admin_type = admin_type)

@site.route('/account')
def admin_account():
    users = User.query.all()
    return render_template('admin/admin_user.html',
                           users = users)

@site.route('/article')
def admin_article():
    articles = Articles.query.all()
    return render_template('admin/admin_article.html',
                           articles = articles)

@site.route('/question')
def admin_question():
    questions = Questions.query.all()
    return render_template('admin/admin_question.html',
                           questions = questions)

@site.route('/comment')
def admin_comment():
    comments = Comments.query.all()
    print(comments)
    return render_template('admin/admin_comment.html',
                           comments = comments)


@site.route('/page_views')
def admin_view():
    categories = Category.query.all()
    return render_template('admin/admin_view.html',
                           categories = categories)

@site.route('/views<title>')
def admin_views(title):
    article = Articles.query.filter_by(title=title).first()
    tags = article.tag_article
    content = Markup(markdown.markdown(article.content))
    return render_template('admin/page.html',
                           article = article,
                           content = content,
                           tags = tags)
