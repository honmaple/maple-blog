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
from ..models import Articles, db, User, Comments, Questions, Tags, Notices
from ..forms import ArticleForm, QuestionForm, EditRegisterForm, NoticesForm
from ..utils import super_permission
from ..utils import DeleteManager, EditManager
from ..utils import get_online_users, get_visited_users
from datetime import datetime

site = Blueprint('admin', __name__, url_prefix='/admin')


def count_sum(count):
    '''文章总数'''
    if count % 10 == 0:
        count = int(count/10)
    else:
        count = int(count/10) + 1
    return count


@site.route('/')
@super_permission.require(404)
def index():
    user_online = get_online_users()
    user_visited = get_visited_users()
    if user_online is None:
        user_online = b'127.0.0.1'
    return render_template('admin/admin.html',
                           user_online=user_online,
                           user_visited=user_visited)


@site.route('/delete/record=<ip>')
@super_permission.require(404)
def delete_ip(ip):
    '''删除记录'''
    from ..utils import delete_visited_users
    delete_visited_users(ip)
    return redirect(url_for('admin.index'))


@site.route('/delete/page/record=<ip>')
@super_permission.require(404)
def delete_page(ip):
    '''删除记录'''
    from ..utils import delete_visited_pages
    delete_visited_pages(ip)
    return redirect(url_for('admin.index'))


@site.route('/add/blacklist=<ip>')
@super_permission.require(404)
def add_blacklist(ip):
    '''加入黑名单'''
    from ..utils import set_blacklist
    set_blacklist(ip)
    return redirect(url_for('admin.index'))


@site.route('/add/writelist=<ip>')
@super_permission.require(404)
def add_writelist(ip):
    '''加入白名单'''
    from ..utils import set_writelist
    set_writelist(ip)
    return redirect(url_for('admin.index'))


@site.route('/notice_post', methods=['GET', 'POST'])
@super_permission.require(404)
def post_notice():
    '''发布公告'''
    notices = Notices.query.all()
    form = NoticesForm()
    if form.validate_on_submit() and request.method == "POST":
        post_notice = Notices(notice=form.notice.data)
        post_notice.publish = datetime.now()
        db.session.add(post_notice)
        db.session.commit()
        flash('已提交')
        return redirect(url_for('admin.post_notice'))
    return render_template('admin/admin_notice.html',
                           form=form,
                           notices=notices)


@site.route('/pages_post', methods=['GET', 'POST'])
@super_permission.require(404)
def admin_post():
    '''增加文章'''
    articles = Articles.query.all()
    form = ArticleForm()
    if form.validate_on_submit() and request.method == "POST":
        '''分类节点'''
        tags = form.tags.data.split(',')
        post_tags = []
        for tag in tags:
            '''判断节点是否存在'''
            # existed_tag = Tags.query.filter_by(name=tag).first()
            # if existed_tag:
            # t = existed_tag
            # else:
            t = Tags(name=tag)
            post_tags.append(t)
        post_article = Articles(user=current_user.name,
                                title=form.title.data,
                                category=form.category.data,
                                content=form.content.data)
        post_article.publish = datetime.now()
        post_article.copy = form.copy.data
        '''关系数据表'''
        post_article.tag_article = post_tags
        db.session.add(post_article)
        db.session.commit()
        flash('已提交')
        return redirect(url_for('admin.admin_post'))
    return render_template('admin/admin_post.html',
                           form=form,
                           articles=articles)


@site.route('/account', defaults={'number': 1})
@site.route('/account/<int:number>')
@super_permission.require(404)
def admin_account(number):
    users = User.query.order_by(User.registered_time.desc()).\
        offset((number-1)*10).limit(10)
    count = User.query.count()
    count = count_sum(count)
    number = number
    return render_template('admin/admin_user.html',
                           users=users,
                           count=count,
                           number=number)


@site.route('/article', defaults={'number': 1})
@site.route('/article/<int:number>')
@super_permission.require(404)
def admin_article(number):
    articles = Articles.query.order_by(Articles.publish.desc()).\
        offset((number-1)*10).limit(10)
    count = Articles.query.count()
    count = count_sum(count)
    number = number
    return render_template('admin/admin_article.html',
                           articles=articles,
                           count=count,
                           number=number)


@site.route('/question', defaults={'number': 1})
@site.route('/question/<int:number>')
@super_permission.require(404)
def admin_question(number):
    questions = Questions.query.order_by(Questions.publish.desc()).\
        offset((number-1)*10).limit(10)
    count = Questions.query.count()
    count = count_sum(count)
    number = number
    return render_template('admin/admin_question.html',
                           questions=questions,
                           count=count,
                           number=number)


@site.route('/comment', defaults={'number': 1})
@site.route('/comment/<int:number>')
@super_permission.require(404)
def admin_comment(number):
    comments = Comments.query.order_by(Comments.publish.desc()).\
        offset((number-1)*10).limit(10)
    count = Comments.query.count()
    count = count_sum(count)
    number = number
    return render_template('admin/admin_comment.html',
                           comments=comments,
                           count=count,
                           number=number)


@site.route('/<category>/<post_id>/delete')
@super_permission.require(404)
def admin_delete(category, post_id):
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
def admin_edit(category, post_id):
    if category == 'article':
        article = Articles.query.filter_by(id=post_id).first()
        form = ArticleForm()
        form.content.data = article.content
        form.title.data = article.title
        form.category.data = article.category
        '''得到节点内容'''
        tags = ''
        leng = 1
        for tag in article.tags:
            if leng == article.tags.count():
                tags += tag.name
            else:
                tags += tag.name + ','
            leng += 1
        form.tags.data = tags
    if category == 'question':
        question = Questions.query.filter_by(id=post_id).first()
        form = QuestionForm()
        form.title.data = question.title
        form.describ.data = question.describ
        form.answer.data = question.answer
    if category == 'user':
        user = User.query.filter_by(id=post_id).first()
        form = EditRegisterForm()
        form.name.data = user.name
        form.roles.data = user.roles
        form.is_superuser.data = str(user.is_superuser)
        form.is_confirmed.data = str(user.is_confirmed)

    category = category
    post_id = post_id
    return render_template('admin/admin_edit.html',
                           form=form,
                           category=category,
                           post_id=post_id)


@site.route('/<category>/<post_id>/save', methods=['GET', 'POST'])
@super_permission.require(404)
def admin_edit_save(category, post_id):
    if category == 'article':
        form = ArticleForm()
    elif category == 'question':
        form = QuestionForm()
    else:
        form = EditRegisterForm()

    action = EditManager(post_id, form)

    if form.validate_on_submit() and request.method == "POST":
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
