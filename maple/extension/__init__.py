#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-01-25 11:48:39 (CST)
# Last Update: Monday 2019-09-23 17:13:53 (CST)
#          By:
# Description:
# ********************************************************************************
from flask_maple.redis import Redis
from flask_maple.mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_caching import Cache
from flask_maple.models import db
from flask_cors import CORS
from . import maple, login, babel

db = db
csrf = CSRFProtect()
cache = Cache()
mail = Mail()
redis = Redis()
cors = CORS()


def init_app(app):
    db.init_app(app)
    csrf.init_app(app)
    cors.init_app(app)
    cache.init_app(app)
    mail.init_app(app)
    redis.init_app(app)
    maple.init_app(app)
    login.init_app(app)
    babel.init_app(app)
