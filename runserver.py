#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: runserver.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2015-11-14 21:19:56 (CST)
# Last Update: 星期六 2018-02-10 13:55:36 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import current_app
from flask.cli import FlaskGroup, run_command
from flask_migrate import Migrate
from werkzeug.contrib.fixers import ProxyFix
from code import interact
from getpass import getpass
from maple.extension import db, cache
from maple import create_app
from maple.model import User
import click
import os
import sys

app = create_app('config')
app.wsgi_app = ProxyFix(app.wsgi_app)

cli = FlaskGroup(add_default_commands=False, create_app=lambda r: app)
cli.add_command(run_command)

migrate = Migrate(app, db)


@cli.command('shell', short_help='Starts an interactive shell.')
def shell_command():
    ctx = current_app.make_shell_context()
    interact(local=ctx)


@cli.command()
def runserver():
    app.run()


@cli.command()
def clear_cache():
    cache.clear()


@cli.command()
def initdb():
    """
    Drops and re-creates the SQL schema
    """
    db.drop_all()
    db.configure_mappers()
    db.create_all()
    db.session.commit()


@cli.command()
@click.option('-l', '--lang', default='zh')
def babel_init(lang):
    babel_conf = "LANG/babel.cfg"
    src_path = ["maple", "templates"]
    os.system('pybabel extract -F {0} -k lazy_gettext -o messages.pot {1}'.
              format(babel_conf, ' '.join(src_path)))
    os.system('pybabel init -i messages.pot -d LANG -l {0}'.format(lang))
    os.unlink('messages.pot')


@cli.command()
def babel_update():
    babel_conf = "LANG/babel.cfg"
    src_path = ["maple", "templates"]
    os.system('pybabel extract -F {0} -k lazy_gettext -o messages.pot {1}'.
              format(babel_conf, ' '.join(src_path)))
    os.system('pybabel update -i messages.pot -d LANG')
    os.unlink('messages.pot')


@cli.command()
def babel_compile():
    os.system('pybabel compile -d LANG')


@cli.command()
@click.option('-u', '--username')
@click.option('-e', '--email')
@click.option('-w', '--password')
def create_user(username, email, password):
    if username is None:
        username = input('Username(default admin):') or 'admin'
    if email is None:
        email = input('Email:')
    if password is None:
        password = getpass('Password:')
    user = User(
        username=username, email=email, is_superuser=True, is_confirmed=True)
    user.set_password(password)
    user.save()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        app.run()
    else:
        cli.main()
