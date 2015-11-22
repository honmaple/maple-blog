#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: assets.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-08 06:08:21
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask.ext.assets import Bundle, Environment
from .. import create_app

app = create_app()

bundles = {

    'home_js': Bundle(
        'js/jquery.min.js',      #这里直接写static目录的子目录 ,如static/bootstrap是错误的
        'js/bootstrap.min.js',
        output='assets/home.js',
        filters='jsmin'),

    'home_css': Bundle(
        'css/bootstrap.min.css',
        output='assets/home.css',
        filters='cssmin')
    }

assets = Environment(app)
assets.register(bundles)
