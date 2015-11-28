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
    SECURITY_PASSWORD_SALT = 'my_precious_two'

    #FLATPAGES_ROOT = '../app/pages'
    FLATPAGES_AUTO_RELOAD = True
    FLATPAGES_EXTENSION = '.md'

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "1171501218@qq.com"
    MAIL_PASSWORD = "mwhduhlgimfgfgfc"
    MAIL_DEFAULT_SENDER = '1171501218@qq.com'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:qaz123@localhost/Books'
    RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
    RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'users': 'postgresql://postgres:qaz123@localhost/Userdb',
        'books': 'postgresql://postgres:qaz123@localhost/Books',
        'mkds': 'postgresql://postgres:qaz123@localhost/mkdb',
        'articles': 'postgresql://postgres:qaz123@localhost/article'
    }

