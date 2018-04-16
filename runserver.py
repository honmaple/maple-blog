#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: runserver.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2015-11-14 21:19:56 (CST)
# Last Update: Saturday 2018-04-16 11:56:35 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import current_app
from flask.cli import FlaskGroup, run_command
from flask_migrate import Migrate
from werkzeug.contrib.fixers import ProxyFix
from code import interact
from getpass import getpass
from random import choice, sample, randrange
from string import ascii_letters, digits

from maple.extension import db, cache
from maple import create_app
from maple.model import User, Blog, Tag, Category, TimeLine

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
def random_init():
    def random_sep(n=6):
        sep = [' '] * n
        sep.append("\n")
        sep.append("\n\n")
        return choice(sep)

    def random_word(n=20, sep=True):
        word = ''.join(sample(ascii_letters + digits, randrange(2, n)))
        if not sep:
            return word
        return word + random_sep()

    random_users = [User(
        username=random_word(12, False),
        password=random_word(12, False),
        email=random_word(15, False)) for _ in range(4)]
    random_tags = [Tag(name=random_word(12, False)) for i in range(15)]
    random_categories = [Category(name=random_word(12, False))
                         for i in range(5)]

    db.session.bulk_save_objects(random_users)
    db.session.bulk_save_objects(random_tags)
    db.session.bulk_save_objects(random_categories)
    db.session.commit()

    random_users = User.query.all()
    random_tags = Tag.query.all()

    for category in Category.query.all():
        print(category, category.id)
        random_blogs = [Blog(
            category_id=category.id,
            title=random_word(20, False),
            content=' '.join([random_word() for _ in range(1000)]),
            user_id=choice(random_users).id,
            tags=[choice(random_tags) for _ in range(randrange(1, 4))])
                        for _ in range(randrange(3, 15))]
        db.session.bulk_save_objects(random_blogs)
        db.session.commit()

    random_timelines = [TimeLine(
        content=' '.join([random_word() for _ in range(100)]),
        user_id=choice(random_users).id,
        is_hidden=choice([True, False])) for _ in range(100)]

    db.session.bulk_save_objects(random_timelines)
    db.session.commit()


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


@cli.command()
@click.option('-u', '--username')
def token(username):
    r = User.query.filter_by(username=username).first().token
    print(r)


@cli.command()
def list_routers():
    table = [["URL", "METHOD", "ENDPOINT"]]
    s_max = [25, 25, 25]
    for rule in app.url_map.iter_rules():
        name = rule.rule
        if len(name) > s_max[0]:
            s_max[0] = len(name)
        method = ",".join(rule.methods)
        if len(method) > s_max[1]:
            s_max[1] = len(method)
        endpoint = rule.endpoint
        if len(method) > s_max[2]:
            s_max[2] = len(endpoint)
        table.append([name, method, endpoint])
    s_max = [i + 2 for i in s_max]
    for t in table:
        print("|{0}|{1}|{2}|".format(* ["-" * s_max[i] for i in range(3)]))
        print("|{0}|{1}|{2}|".format(* [t[i] + " " * (s_max[i] - len(t[i]))
                                        for i in range(3)]))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        app.run()
    else:
        cli.main()
