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
    url_for,flash,request,g,current_app,session,abort
from flask_login import login_user, logout_user, \
    current_user, login_required
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed
from werkzeug.security import check_password_hash,generate_password_hash
from app import login_manager
from ..email import email_token,email_send,confirm_token,email_validate
from ..models import User,Questions,Comments,Articles,db
from ..forms import LoginForm,RegisterForm,NewPasswdForm,\
    EditUserInforForm,ForgetPasswdForm
from ..utils import EditManager,writer_permission,check_overtime
from datetime import datetime

site = Blueprint('index',__name__,url_prefix='')

@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))

@site.route('/')
@site.route('/index')
def index():
    '''主页'''
    articles = Articles.query.order_by(Articles.publish.desc()).limit(7)
    questions = Questions.query.order_by(Questions.publish.desc()).\
        filter_by(private=False).limit(7)
    return render_template('index/index.html',
                           articles = articles,
                           questions = questions)

@site.route('/login', methods=['GET','POST'])
def login():
    '''登陆'''
    error = None
    form = LoginForm()
    '''验证码'''

    # validate = ValidateCode()
    # validate.start()
    # if session['code']:
        # validate_code = session['code']
    # else:
        # session['code'] = 'Welcome To HonMaple'
        # validate_code = None
    '''如果已经登陆则重定向到主页'''
    if g.user is not None and g.user.is_authenticated:
        flash('你已经登陆,不能重复登陆')
        return redirect(url_for('index.index'))
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(name=form.name.data).first()
        # if form.validate_code.data.lower()  == validate_code.lower():
        if user:
            if not check_password_hash(user.passwd, form.passwd.data):
                error = u'密码错误'
            else:
                if form.remember_me.data:
                    '''cookie加密'''
                    session.permanent = True
                    session['name'] = generate_password_hash(form.name.data)

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
    session.clear()
    for key in ('identity.id', 'identity.auth_type'):
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
    if form.validate_on_submit() and request.method == "POST":
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
            account.registered_time = datetime.now()

            '''邮箱验证'''
            token = email_token(account.email)
            '''email模板'''
            confirm_url = url_for('index.confirm', token=token, _external=True)
            html = render_template('templet/email.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            email_send(account.email,html,subject)
            flash('一封验证邮件已发往你的邮箱，請查收.', 'success')

            account.send_email_time = datetime.now()
            db.session.add(account)
            db.session.commit()

            login_user(account)
            identity_changed.send(current_app._get_current_object(),
                            identity=Identity(account.id))
            return redirect(url_for('index.logined_user',name=account.name))
    return render_template('index/sign_in.html',form=form,error=error)

@site.route('/confirm_email')
@login_required
@check_overtime
def confirm_email():
    if current_user.is_confirmed:
        flash('你的账户已验证,不能重复验证')
        return redirect(url_for('index.logined_user',name=current_user.name))

    token = email_token(current_user.email)
    '''email模板'''
    confirm_url = url_for('index.confirm', token=token, _external=True)
    html = render_template('templet/email.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    email_send(current_user.email,html,subject)
    flash('一封验证邮件已发往你的邮箱，請查收.', 'success')

    current_user.send_email_time = datetime.now()
    db.session.commit()
    return redirect(url_for('index.logined_user',name=current_user.name))


@site.route('/confirm/<token>')
@login_required
def confirm(token):
    email = confirm_token(token)
    if not email:
        flash('验证链接已过期,请重新获取', 'danger')
        abort(404)

    user = User.query.filter_by(email=email).first()
    if user.is_confirmed:
        flash('账户已经验证. Please login.', 'success')
    else:
        user.is_confirmed = True
        user.confirmed_time = datetime.now()
        '''账户验证后可以评论'''
        user.roles = 'writer'
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('index.logined_user',name=user.name))

@site.route('/forget',methods=['GET','POST'])
def forget():
    '''忘记密码'''
    form = ForgetPasswdForm()
    if form.validate_on_submit() and request.method == "POST":
        '''验证邮箱格式'''
        email_format = email_validate(form.confirm_email.data)
        if email_format:
            '''邮箱是否存在'''
            exsited_email = User.query.filter_by(email=\
                                                form.confirm_email.data).first()
            if exsited_email:
                token = email_token(form.confirm_email.data)
                '''email模板'''
                confirm_url = url_for('index.forget_confirm', token=token, _external=True)
                html = render_template('templet/forget.html', confirm_url=confirm_url)
                subject = "Please revise your password"
                email_send(form.confirm_email.data,html,subject)
                flash('邮件已发送到你的邮箱')
                return redirect(url_for('index.index'))
            else:
                flash('邮箱未注册')
        else:
            flash('邮箱格式错误')
    return render_template('index/forget.html',
                           form=form)

@site.route('/forget/<token>',methods=['GET','POST'])
def forget_confirm(token):
    form = NewPasswdForm()
    '''验证链接'''
    email = confirm_token(token)
    if not email:
        flash('验证链接已过期,请重新获取', 'danger')
        abort(404)

    exsited_user = User.query.filter_by(email=email).first()
    if form.validate_on_submit() and request.method == "POST":
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
                           token = token)


@site.route('/u/<name>/view')
@login_required
def logined_user(name):
    '''不能进别人主页'''
    if current_user.name != name:
        abort(404)
    user_questions = Questions.query.filter_by(user=name).all()
    user_comments = Comments.query.filter_by(user=name).all()
    user = User.query.filter_by(name=name).first()
    form = EditUserInforForm()
    form.school.data = user.school
    form.introduce.data = user.introduce
    return render_template('user/user.html',
                            form = form,
                            user = user,
                            user_comments = user_comments,
                            user_questions = user_questions)

@site.route('/u/<post_id>/edit',methods=['GET','POST'])
@login_required
@writer_permission.require(404)
def user_infor_edit(post_id):
    form = EditUserInforForm()
    action = EditManager(post_id,form)
    if request.method == "POST":
        user = User.query.filter_by(id=post_id).first()
        if check_password_hash(user.passwd, form.passwd.data):
            '''如果修改密码'''
            if form.new_passwd.data or form.retry_new_passwd.data:
                if form.retry_new_passwd.data == form.new_passwd.data:
                    action.edit_user_infor()
                    flash('资料更新成功,请重新登陆')
                    '''修改密码后重新登陆'''
                    logout_user()
                    for key in ('identity.id', 'identity.auth_type'):
                        session.pop(key, None)
                    identity_changed.send(current_app._get_current_object(),
                            identity=AnonymousIdentity())
                    return redirect(url_for('index.login'))
                else:
                    flash('两次密码输入不一致，请重新输入')
            else:
                '''没有修改密码'''
                user.school = form.school.data
                user.introduce = form.introduce.data
                db.session.commit()
        else:
            flash('密码错误，请重新输入')
        return redirect(url_for('index.logined_user',
                                name=user.name,
                                _anchor='secure'))
    return redirect(url_for('index.index'))


# @site.route('/search',methods=['GET','POST'])
# def search():
    # form = SearchForm()
    # if request.method == "POST":
        # search_content = '%%%s%%'%form.content.data
        # print(search_content)
        # results = Articles.query.filter(Articles.content.like(search_content)).all()
        # print(results)
        # # return redirect(url_for('index.search',results=results))
    # return render_template('index/search.html',
                           # results = results)

# @site.route('/validate')
# def validate_code():
    # validate = ValidateCode()
    # validate_name = validate.start()
    # return 'static/images/' + validate_name
    # return send_file('static/images/validate.png',
                     # mimetype='image/png')

@site.route('/about')
def about():
    about = Articles.query.filter_by(id=26).first()
    content = about.content
    return render_template('index/about_me.html',
                           content = content)

