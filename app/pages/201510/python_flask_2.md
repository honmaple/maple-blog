Title: flask学习笔记--2
Author: honmaple 
Date: 2015-10-25
Category: python
Tags: [ python,flask ]
Slug: python_flask_2
Summary : 今天被flask的项目结构或者说是蓝图搞得晕头转脑，各种文档也没说清，从github搜索并clone了几个用flask做成的网站，无奈水平太低，看不懂

*今天被flask的项目结构或者说是蓝图搞得晕头转脑，各种文档也没说清，从github搜索并clone了几个用flask做成的网站，无奈水平太低，看不懂*

记录一下今天学到的

## 蓝图
|-app/  
|-|__init__.py
|-|views.py  
|-|__init__.py  
|-|templates/  
|-|static/  
|-config.py  
|-run.py  
|-tmp/  

### run.py
输入`python run.py`就可以运行程序

    from app import app #从app包中调用app模块
    app.run() #运行程序

### config.py
一些基本的配置

    DEBUG = True #打开调试模式

### app/__init__.py

    from flask import Flask, request, session, g, redirect, url_for, \
         abort, render_template, flash

    app = Flask(__name__)
    app.config.from_object("config")  #调用config.py配置文件

    from app import views #从app包中导入views模块

### app/views.py
视图文件

    from app import app
    from flask import Flask, request, session, g, redirect, url_for, \
         abort, render_template, flash
    @app.route.('/')
    def Index():
        return 'hello,world'
    @app.route(/index)
    def Show_page():
        return render_template('index.html')

### app/templates/
放置模板

### app/templates/index.html

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
            #使用static文件夹中的css，js
            <title>
            hello
            </title>
            
        </head>
        <body>
            <ul>
                <li>hello</li>
                <li>world</li>
                <li>hello world</li>
            </ul>
        </body>
    </html>

### app/static
放置一些静态文件
css,js等












