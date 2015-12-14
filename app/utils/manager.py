#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: manager.py
#   Author:JiangLin 
#   Mail:xiyang0807@gmail.com 
#   Created Time: 2015-12-13 19:57:29
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from ..models import Comments,Articles,Replies,User,Questions,db

class DeleteManager(object):
    def __init__(self,post_id):
        self.post_id = post_id

    def delete_user(self):
        '''删除用户'''
        user = User.query.filter_by(id=self.post_id).first()
        db.session.delete(user)
        db.session.commit()

    def delete_article(self):
        '''删除文章'''
        article = Articles.query.filter_by(id=self.post_id).first()
        tags = []
        for tag in article.tags:
            tags.append(tag)
            article.tags.remove(tag)
        db.session.commit()

        for tag in tags:
            db.session.delete(tag)
        db.session.delete(article)
        db.session.commit()

    def delete_question(self):
        '''删除问题'''
        question = Questions.query.filter_by(id=self.post_id).first()
        db.session.delete(question)
        db.session.commit()

    def delete_comment(self):
        '''删除评论'''
        comment = Comments.query.filter_by(id=self.post_id).first()
        db.session.delete(comment)
        db.session.commit()

    def delete_reply(self):
        '''删除回复'''
        reply = Replies.query.filter_by(id=self.post_id).first()
        db.session.delete(reply)
        db.session.commit()


class EditManager(object):
    def __init__(self,post_id,form):
        self.post_id = post_id
        self.form = form

    def edit_user(self):
        '''编辑用户'''
        user = User.query.filter_by(id=self.post_id).first()
        user.name = self.form.name.data
        user.is_superuser = self.form.is_superuser.data
        user.roles = self.form.roles.data
        user.is_confirmed = self.form.is_confirmed.data
        db.session.commit()

    def edit_article(self):
        '''编辑文章'''
        article = Articles.query.filter_by(id=self.post_id).first()
        article.title = self.form.title.data
        article.summary = self.form.summary.data
        article.content = self.form.content.data
        article.title = self.form.title.data
        db.session.commit()

    def edit_question(self):
        '''编辑问题'''
        question = Questions.query.filter_by(id=self.post_id).first()
        question.title = self.form.title.data
        question.describ = self.form.describ.data
        question.answer = self.form.answer.data
        db.session.commit()

