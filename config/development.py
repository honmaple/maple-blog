#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: config.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-10-25 08:01:06
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = 'you-will-never-guess'
    #FLATPAGES_ROOT = '../app/pages'
    FLATPAGES_AUTO_RELOAD = True
    FLATPAGES_EXTENSION = '.md'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:qaz123@localhost/Books'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'users': 'postgresql://postgres:qaz123@localhost/Userdb',
        'books': 'postgresql://postgres:qaz123@localhost/Books',
        'mkds': 'postgresql://postgres:qaz123@localhost/mkdb'
    }

