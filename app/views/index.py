#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: index.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 02:21:04
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import render_template, Blueprint,redirect, \
    url_for,flash,request,g,Markup,current_app,session,abort
from flask_login import login_user, logout_user, \
    current_user, login_required
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed
from werkzeug.security import check_password_hash,generate_password_hash
from ..email import email_token,email_send,confirm_token,email_validate
from app import login_manager
from ..models import User,Questions,Comments,db
from ..forms import LoginForm,RegisterForm
from ..utils import writer_permission,EditManager
import datetime
import markdown



site = Blueprint('index',__name__,url_prefix='')

@site.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))

@site.route('/')
@site.route('/index')
def index():
    '''主页'''
    return render_template('index/index.html')

@site.route('/login', methods=['GET','POST'])
def login():
    '''登陆'''
    error = None
    form = LoginForm()
    '''验证码'''
    # validate = ValidateCode()
    # validate_code = validate.start()
    # print(validate_code[1])
    '''如果已经登陆则重定向到主页'''
    if g.user is not None and g.user.is_authenticated:
        flash('你已经登陆,不能重复登陆')
        return redirect(url_for('index.index'))
    if request.method == 'POST':
        user = User.query.filter_by(name=form.name.data).first()
        # if form.validate_code.data == validate_code[1]:
        if user:
            if not check_password_hash(user.passwd, form.passwd.data):
                error = u'密码错误'
            else:
                login_user(user)

                identity_changed.send(current_app._get_current_object(),
                                identity=Identity(user.id))
                flash('你已成功登陆.')
                '''next是必需的,登陆前请求的页面'''
                return redirect(request.args.get('next') or url_for('index.index'))
        else:
            error = u'用户名错误'
        # else:
            # error = u'验证码错误'
    return render_template('index/login.html',
                           form=form,
                           error = error)

@site.route('/logout')
@login_required
def logout():
    '''注销'''
    logout_user()
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())
    return redirect(request.args.get('next') or url_for( 'index.index'))


@site.route('/sign', methods=['GET','POST'])
def sign():
    '''注册账户'''
    error = None
    form = RegisterForm()
    if g.user is not None and g.user.is_authenticated:
        flash('你已经登陆,不能重复登陆')
        return redirect(url_for('index.index'))
    if request.method == 'POST':
        useremail = User.query.filter_by(email=form.email.data).first()
        username = User.query.filter_by(name=form.name.data).first()
        email_format = email_validate(form.email.data)
        if username:
            error = u'用户名已存在'
        elif useremail:
            error = u'邮箱已被注册'
        elif email_format == False:
            error = u'邮箱格式错误'
        elif not form.name.data or not form.email.data:
            error = u'输入不能为空'
        else:
            account = User(name = form.name.data,
                           email = form.email.data,
                           passwd = form.passwd.data,
                           roles = 'visitor')
            db.session.add(account)
            db.session.commit()

            '''邮箱验证'''
            token = email_token(account.email)
            login_user(account)
            '''email模板'''
            confirm_url = url_for('index.confirm', token=token, _external=True)
            html = render_template('email.html', confirm_url=confirm_url)
            email_send(account.email,html)

            flash('一封验证邮件已发往你的邮箱，請查收.', 'success')
            return redirect(url_for('index.logined_user',name=account.name))
    return render_template('index/sign_in.html',form=form,error=error)

@site.route('/confirm/<token>')
@login_required
def confirm(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.is_confirmed:
        flash('账户已经验证. Please login.', 'success')
    else:
        user.is_confirmed = True
        user.confirmed_time = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('index.logined_user',name=user.name))

@site.route('/forget',methods=['GET','POST'])
def forget():
    form = RegisterForm()
    if request.method == 'POST':
        '''加密的验证链接'''
        exsited_email = User.query.filter_by(email=\
                                             form.confirm_email.data).first()
        print(form.confirm_email.data)
        if exsited_email:
            token = email_token(form.confirm_email.data)
            '''email模板'''
            confirm_url = url_for('index.forget_confirm', token=token, _external=True)
            html = render_template('forget.html', confirm_url=confirm_url)
            email_send(form.confirm_email.data,html)
            flash('邮件已发送到你的邮箱')
        else:
            flash('邮箱未注册')
    return render_template('index/forget.html',
                           form=form)

@site.route('/forget/<token>')
def forget_confirm(token):
    form = RegisterForm()
    email = confirm_token(token)
    if not email:
        abort(404)
    return render_template('index/revise_passwd.html',
                           form=form,
                           email = email)

@site.route('/revise/<email>',methods=['GET','POST'])
def revise_passwd(email):
    form = RegisterForm()
    exsited_user = User.query.filter_by(email=email).first()
    if request.method == 'POST':
        if form.retry_new_passwd.data != form.new_passwd.data:
            flash('两次密码不一致,请重新输入')
        else:
            new_passwd = form.retry_new_passwd.data
            exsited_user.passwd = generate_password_hash(new_passwd)
            db.session.commit()
            flash('密码修改成功,请登录')
            return redirect(url_for('index.login'))
    return render_template('index/revise_passwd.html',
                           form=form,
                           email = email)



@site.route('/u/<name>/view')
@login_required
def logined_user(name):
    '''不能进别人主页'''
    if current_user.name != name:
        abort(404)
    user_questions = Questions.query.filter_by(user=name).all()
    user_comments = Comments.query.filter_by(user=name).all()
    user = User.query.filter_by(name=name).first()
    form = RegisterForm()
    form.email.data = user.email
    return render_template('user/user.html',
                            form = form,
                            user = user,
                            user_comments = user_comments,
                            user_questions = user_questions)

@site.route('/u/<post_id>/edit',methods=['GET','POST'])
@login_required
def user_infor_edit(post_id):
    form = RegisterForm()
    action = EditManager(post_id,form)
    if request.method == 'POST':
        user = User.query.filter_by(id=post_id).first()
        if check_password_hash(user.passwd, form.passwd.data):
            if form.retry_new_passwd.data == form.new_passwd.data:
                action.edit_user_infor()
                flash('资料更新成功')
            else:
                flash('两次密码输入不一致，请重新输入')
        else:
            flash('密码错误，请重新输入')
    return redirect(url_for('index.logined_user',name=user.name))


@site.route('/about')
@writer_permission.require(http_exception=403)
def about():
    content = """
### **个人介绍**

#### 我是一个爱好自由的人,目前正在读大三,专业自动化

### **目前技能**  

#### python: 熟悉基本语法，熟悉re,BeautifulSoup,request,flask等模块
#### html/css: 能够熟练掌握,并用html/css写出较漂亮的网页
#### Javascript: 基本语法
#### C: 对于除链表之外的内容熟练掌握
#### linux: 掌握linux基本命令，能够利用linux搭建基础服务 并且日常使用
#### 数据库: 熟悉数据库相关的基础知识，熟悉 sqlite,postgresql

### **项目**

#### 利用python爬虫爬取豆瓣读书，学校新闻，图书馆书籍等  
[项目链接]( https://github.com/honmaple/python )

#### 利用flask搭建个人网站(就是现在这个网站)  
>前端大部分采用bootstrap模板，少部分自己写的布局  
后端利用flask + gunicorn + supervisord + ngnix + postgresql  
博客文章利用markdown标记语言  
书籍查询抓取自豆瓣读书  

[项目链接](https://github.com/honmaple/website)

### **联系方式**  

#### Mail:xiyang0807@gmail.com
#### Github主页:<https://github.com/honmaple>
"""
    content = Markup(markdown.markdown(content))
    return render_template('index/about_me.html',**locals())

