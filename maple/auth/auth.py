#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: auth.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-02 11:53:15 (CST)
# Last Update:星期四 2016-6-2 11:56:55 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple import Auth
from maple import app, db, mail
from maple.user.models import User
from datetime import datetime


class Login(Auth):
    def register_models(self, form):
        user = self.User()
        user.username = form.username.data
        user.password = user.set_password(form.password.data)
        user.email = form.email.data
        user.roles = 'visitor'
        user.registered_time = datetime.now()
        user.send_email_time = datetime.now()
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def confirm_models(self, user):
        user.is_confirmed = True
        user.confirmed_time = datetime.now()
        user.roles = 'writer'
        self.db.session.commit()


Login(app, db=db, mail=mail, user_model=User, use_principal=True)
