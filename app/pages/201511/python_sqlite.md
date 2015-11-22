Title: flask学习——数据库操作
Author: honmaple 
Date: 2015-11-10
Category: python
Tags: [ python,flask ]
Slug: python_sqlite
Summary : flask 作为后端数据库操作是必要的，现在记录一下一些flask数据库的相关操作</br>暂时使用较简单的sqlite作为例子


flask 作为后端数据库操作是必要的，现在记录一下一些flask数据库的相关操作，
我将使用三种方法操作数据库  
暂时使用较简单的sqlite作为例子
## 相关环境的安装
*建议使用ve虚拟环境*

    sudo pacman -S sqlite # archlinux
    sudo pip install virtualenv 
    # 在vertualenv环境下执行
    pip install Flask-SQLAlchemy Jinja2 SQLAlchemy 
**最好是多看文档**

## 1.使用sqlite3模块API
[参考资料](http://www.runoob.com/sqlite/sqlite-python.html)  
*这是最简单的方法,不仅适用于flask,python的其他方面也一样适用,如爬虫之类*  

#### 连接数据库
    #!/usr/bin/env python
    # -*- coding=UTF-8 -*-
    import sqlite3
    database = /path/test.db  #数据库文件路径
    test = sqlite.connect('database') #连接数据库，如果数据库文件不存在则创建
    print('connect database successfully')
    test.close()  #关闭数据库连接
如果将数据库名改为**:memory:**,则在内存中打开数据库而不是磁盘

#### 创建表
    database = /path/test.db
    test = sqlite.connect('database')
    test.execute('''CREATE TABLE BOOKS
           (ID INT PRIMARY KEY     NOT NULL,
           TYPE           TEXT    NOT NULL,
           NAME           TEXT    NOT NULL,
           CONTENT        TEXT);''')
    print("Table created successfully")
    test.close()

#### 插入数据
    database = /path/test.db
    test = sqlite.connect('database')
    test.execute("INSERT INTO BOOKS (ID,TYPE,NAME,CONTENT) \
          VALUES (1, 'hello', 'world', 'helloworld')");
    test.execute("INSERT INTO BOOKS (ID,TYPE,NAME,CONTENT) \
          VALUES (2, 'goodbye', 'world', 'goodbyeworld')");
    test.commit() #要使数据保存，必须提交
    print("Records commited successfully")
    test.close()
#### 查询数据
    database = /path/test.db
    test = sqlite.connect('database')
    cursor = test.execute("SELECT ID,TYPE,NAME,CONTENT  from BOOKS")
    for row in cursor:
       print("ID =%d "%(row[0]))
       print("TYPE =%s "%(row[1]))
       print("NAME =%s "%(row[2]))
       print("CONTENT =%s "%(row[3]))
    test.close()
#### 更新数据
    database = /path/test.db
    test = sqlite.connect('database')
    test.execute("UPDATE BOOKS SET CONTENT = 'hello' WHERE ID=2")
    test.commit
    test.close()
#### 删除数据
    database = /path/test.db
    test = sqlite.connect('database')
    test.execute("DELETE FROM BOOKS WHERE ID=2")
    test.commit
    test.close()

*由于数据库文件我已经在外部使用第一种方法创建,所以第二种方法我直接打开*
## 2.使用文档上所说的方法
参考资料  
[英文](http://flask.readthedocs.org/en/0.2/patterns/sqlite3/)
[中文](http://docs.jinkan.org/docs/flask/patterns/sqlite3.html)

    import sqlite3
    from flask import g

    DATABASE = '/path/to/database.db'

    def connect_db():
        return sqlite3.connect(DATABASE)

    @app.before_request #使用app_request装饰器打开数据库
    def before_request():
        g.db = connect_db()

    @app.teardown_request #使用app_request装饰器关闭数据库
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()

    def query_db(query, args=(), one=False):  #数据库简化查询
        cur = g.db.execute(query, args)
        rv = [dict((cur.description[idx][0], value)
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv  
需要使用时(主要是查询)  

    for book in query_db('select * from BOOKS'):
        print book['NAME'], 'has the id', book['ID']
    #由于flask一般不使用print，可以这样
    book = query_db('select * from BOOKS')
    在模板中
    {{ book.ID }}或着{{ book['ID'] }}

如果只希望得到一个单独的结果  

    book = query_db('select * from BOOKS where NAME = ?',
                    [the_bookname], one=True)
    if book is None:
        print 'No such user'
    else:
        print the_bookname, 'has the id', book['ID']
创建，更新，插入，删除数据请使用第一个方法  
### 初始化数据库模型
    from contextlib import closing

    def init_db():
        with closing(connect_db()) as db:
            with app.open_resource('schema.sql') as f:
                db.cursor().executescript(f.read())
            db.commit()
        
## 3.使用Flask-SQLAlchemy扩展 (这应该是最推荐的方法)
参考文档  
[中文](http://www.pythondoc.com/flask-sqlalchemy/index.html)
[英文](https://pythonhosted.org/Flask-SQLAlchemy/)
### 一个最小应用
    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # sqlite打开的格式是sql:///三个"/",接着是数据库文件的**绝对路径**
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True)
        email = db.Column(db.String(120), unique=True)

        def __init__(self, username, email):
            self.username = username
            self.email = email

        def __repr__(self):
            return '<User %r>' % self.username

#### 使用
假若上面代码保存为test.py    
    打开python shell

    >>> from test import db,User
    >>> db.create_all() #创建表
    >>> admin = User('admin', 'admin@example.com') #创建数据
    # 这时数据还未真正写入数据库,需要提交
    >>> db.session.add(admin)
    >>> db.session.commit() #这时数据已经写入数据库中
    # 简单数据查询
    >>> users = User.query.all()
    >>> print(users)
    [<User u'admin'>]
    >>> admin = User.query.filter_by(username='admin').first()
    >>> print(admin)
    <User u'admin'>
如果想要简单的查看数据,推荐firefox的一个sqlite插件 **sqlite manager**

#### 配置
    SQLALCHEMY_DATABASE_URI #用于连接的数据库
    SQLALCHEMY_BINDS #连接多个数据库
    # 比如
    SQLALCHEMY_BINDS = {
        'users':        'mysqldb://localhost/users',
        'appmeta':      'sqlite:////path/to/appmeta.db'
    }
    # 创建删除表
    >>> db.create_all(bind=['users'])
    >>> db.create_all(bind='appmeta')
    # 引用绑定,使用 __bind_key__
    class User(db.Model):
        __bind_key__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True)
#### 选择，插入，删除
插入  

    >>> from test import User
    >>> me = User('admin', 'admin@example.com')
    >>> db.session.add(me)
    >>> db.session.commit()
删除  

    >>> db.session.delete(me)
    >>> db.session.commit()
查询  
首先插入如下数据

|id       |username | email           |
|:-------:|:-------:|:---------------:|
|1        |admin    |admin@example.com|
|2        |peter    |peter@example.org|
|3        |guest    |guest@example.com|
通过用户名查询用户:

    >>> admin = User.query.filter_by(username='admin').first()
    >>> print(admin.id)
    1
    >>> print(admin.email)
    u'admin@example.com'
查找不存在的用户名:  

    >>> missing = User.query.filter_by(username='missing').first()
    >>> missing is None
    True

使用更复杂的表达式查询一些用户:  

    >>> User.query.filter(User.email.endswith('@example.com')).all()
    [<User u'admin'>, <User u'guest'>]
按某种规则对用户排序:

    >>> User.query.order_by(User.username)
    [<User u'admin'>, <User u'guest'>, <User u'peter'>]
限制返回用户的数量:

    >>> User.query.limit(1).all()
    [<User u'admin'>]
用主键查询用户:

    >>> User.query.get(1)
    <User u'admin'>

#### 在视图中使用
使用 get_or_404() 来代替 get()，使用 first_or_404() 来代替 first()。
这样会抛出一个 404 错误，而不是返回 None:

    @app.route('/user/<username>')
    def show_user(username):
        user = User.query.filter_by(username=username).first_or_404()
        return render_template('show_user.html', user=user)

*主要就是这样，最好看完整的文档*  
具体例子可以查看[GitHub](http://github.com/honmaple/flask)
