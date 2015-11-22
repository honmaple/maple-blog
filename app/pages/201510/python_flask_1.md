Title: flask学习笔记--1 
Author: honmaple 
Date: 2015-10-24
Category: python
Tags: [ python,flask ]
Slug: python_flask_1
Summary: flask

## 基本知识
python html/css javascript http等

## flask安装

Flask 依赖两个外部库： Werkzeug 和 Jinja2 。
Werkzeug 是一个 WSGI 套件。 WSGI 是 Web 应用与 多种服务器之间的标准 Python 接口，即用于开发，也用于部署。 
Jinja2 是用于渲染 模板的。

### virtualenv
**关于virtualenv**  

安装 virtualenv  

    $ sudo pip install virtualenv
安装完virtualenv后创建自己的文件夹  

    $ mkdir flask
    $ cd flask
    $ virtualenv venv
    New python executable in env/bin/python
    Installing setuptools............done.
以后要使用virtualenv只用输入  

    $ . venv/bin/activate   #不要忘记了"."
你会发现在终端PS1前会出现(venv),代表你已经进入virtualenv虚拟环境  
退出virtualenv  
    
    $ deactivate
### 在virtualenv中安装flask
    $pip install flask
>另外,你也可以使用`$ sudo pip install flask`安装flask到你的电脑中

## flask使用
安装完后就可以使用了
注意项目结构
>推荐使用  
|-app/  
|-|views.py  
|-|models.py  
|-|__init__.py  
|-|templates/  
|-|static/  
|-config.py  
|-run.py  
|-tmp/  

### 创建第一个应用过过隐
*暂时可以不用进行项目结构编排*

    $vim hello.py
输入

    from flask import Flask
    #导入Flask类
    app = Flask(__name__)
    #__name__模块名，必须的
    @app.route('/')
    #使用 route() 装饰器来告诉 Flask 触发函数的 URL 
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()
    #使用 run() 函数来运行本地服务器和应用  
运行后出现
>\* Running on http://127.0.0.1:5000/  

打开浏览器输入网址<http://127.0.0.1:5000/>

### 打开调试模式
    app.debug = True
    app.run()
或者是  

    app.run(debug=True)
## 注意
>调试模式仅限在本地使用，在生产环境中不要打开
