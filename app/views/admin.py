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
    flash, redirect, url_for
from flask.ext.login import current_user
from ..models import Articles,db,User,Comments,Questions,Tags,Category
from ..forms import ArticleForm,QuestionForm,RegisterForm
from ..utils import super_permission
from ..utils import DeleteManager,EditManager

site = Blueprint('admin',__name__,url_prefix='/admin')

@site.route('/')
@super_permission.require(404)
def index():
   return render_template('admin/admin.html')

@site.route('/pages_post', methods=['GET','POST'])
@super_permission.require(404)
def admin_post():
    articles = Articles.query.all()
    form = ArticleForm()
    if request.method == 'POST':
        '''分类节点'''
        tags = form.tags.data.split(',')
        post_tags = []
        for tag in tags:
            '''判断节点是否存在'''
            # existed_tag = Tags.query.filter_by(name=tag).first()
            # if existed_tag:
                # t = existed_tag
            # else:
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
        flash('已提交')
        return redirect(url_for('admin.admin_post'))
    return render_template('admin/admin_post.html',
                           form=form,
                           articles = articles)

@site.route('/<type>')
@super_permission.require(404)
def types(type):
    return redirect(url_for('index.index'))
    # admin_type = type
    # mkds = Articles.query.all()
    # return render_template('admin/admin_user.html',
                           # mkds = mkds,
                           # admin_type = admin_type)

@site.route('/account')
@super_permission.require(404)
def admin_account():
    users = User.query.all()
    return render_template('admin/admin_user.html',
                           users = users)

@site.route('/article')
@super_permission.require(404)
def admin_article():
    form = ArticleForm()
    articles = Articles.query.all()
    return render_template('admin/admin_article.html',
                           articles = articles,
                           form = form)

@site.route('/question')
@super_permission.require(404)
def admin_question():
    questions = Questions.query.all()
    return render_template('admin/admin_question.html',
                           questions = questions)

@site.route('/comment')
@super_permission.require(404)
def admin_comment():
    comments = Comments.query.all()
    return render_template('admin/admin_comment.html',
                           comments = comments)

@site.route('/<category>/<post_id>/delete')
@super_permission.require(404)
def admin_delete(category,post_id):
    action = DeleteManager(post_id)
    if category == 'article':
        action.delete_article()
        return redirect(url_for('admin.admin_article'))
    elif category == 'comment':
        action.delete_comment()
        return redirect(url_for('admin.admin_comment'))
    elif category == 'reply':
        action.delete_reply()
        return redirect(url_for('admin.admin_comment'))
    elif category == 'user':
        action.delete_user()
        return redirect(url_for('admin.admin_account'))
    elif category == 'question':
        action.delete_question()
        return redirect(url_for('admin.admin_question'))
    else:
        return redirect(url_for('admin.index'))

@site.route('/<category>/<post_id>/edit')
@super_permission.require(404)
def admin_edit(category,post_id):
    if category == 'article':
        article = Articles.query.filter_by(id=post_id).first()
        form = ArticleForm()
        form.content.data = article.content
        form.summary.data = article.summary
        form.title.data = article.title
        tags = []
        for tag in article.tags:
            tags.append(tag.name)
        form.tags.data = tags
    if category == 'question':
        question = Questions.query.filter_by(id=post_id).first()
        form = QuestionForm()
        form.title.data = question.title
        form.describ.data = question.describ
        form.answer.data = question.describ
    if category == 'user':
        user = User.query.filter_by(id=post_id).first()
        form = RegisterForm()
        print(user.roles)
        print(user.is_superuser)
        print(user.is_confirmed)
        form.name.data = user.name
        form.is_superuser.data = user.is_superuser
        form.roles.data = user.roles
        form.is_confirmed.data = user.is_confirmed

    category = category
    post_id = post_id
    return render_template('admin/admin_edit.html',
                           form = form,
                           category = category,
                           post_id = post_id)

@site.route('/<category>/<post_id>/save',methods=['GET','POST'])
def admin_edit_save(category,post_id):
    if category == 'article':
        form = ArticleForm()
    elif category == 'question':
        form = QuestionForm()
    else:
        form = RegisterForm()

    action = EditManager(post_id,form)

    if request.method == 'POST':
        if category == 'article':
            action.edit_article()
            return redirect(url_for('admin.admin_article'))
        elif category == 'question':
            action.edit_question()
            return redirect(url_for('admin.admin_question'))
        elif category == 'user':
            action.edit_user()
            return redirect(url_for('admin.admin_account'))
        else:
            return redirect(url_for('admin.index'))
