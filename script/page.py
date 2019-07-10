#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: page.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-29 01:27:31 (CST)
# Last Update: Wednesday 2019-07-10 20:01:14 (CST)
#          By:
# Description:
# ********************************************************************************
import os
import re
from maple.model import User
from maple.blog.db import Article, Tag, Category
from getpass import getpass
from datetime import datetime


def add_tags(names):
    tags = []
    for name in names:
        name = name.strip()
        tag = Tag.query.filter_by(name=name).first()
        if not tag:
            tag = Tag(name=name)
            tag.save()
        tags.append(tag)
    return tags


def add_category(name):
    name = name.strip()
    name = name.capitalize()
    category = Category.query.filter_by(name=name).first()
    if not category:
        category = Category(name=name)
        category.save()
    return category


def add_author(username):
    username = "honmaple"
    email = "mail@honmaple.com"
    author = User.query.filter_by(username=username).first()
    if not author:
        author = User(
            username=username,
            email=email,
            is_superuser=True,
            is_confirmed=True,
        )
        author.set_password(getpass("Password: "))
        author.save()
    return author


def add_article(title,
                content,
                category,
                author,
                tags,
                date,
                content_type="org-mode"):
    article = Article(
        title=title,
        content=content,
        content_type=content_type,
        category=add_category(category),
        tags=add_tags(tags),
        user=add_author(author),
        created_at=date)
    article.save()
    return article


def time_format(date):
    if ":" in date:
        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return datetime.strptime(date, "%Y-%m-%d")


class Reader(object):
    content_type = Article.CONTENT_TYPE_ORGMODE

    def __init__(self, filename):
        self.filename = filename
        self.attr = dict()

    def parse(self, line):
        return False

    def run(self):
        with open(self.filename) as f:
            lines = f.read()

        is_content = False
        content = []
        for line in lines.splitlines():
            if is_content:
                content.append(line)
                continue

            if not self.parse(line) or not line.strip():
                is_content = True

        attr = {
            "title": self.attr["title"],
            "author": self.attr["title"],
            "category": self.attr["category"],
            "tags": self.attr["tags"].split(","),
            "date": time_format(self.attr["date"]),
            "content": "\n".join(content),
            "content_type": self.content_type
        }
        return attr


class Org(Reader):
    def parse(self, line):
        regex = re.compile(r'^(\s*)#\+(.*): (.*)$')
        if regex.match(line):
            m = regex.match(line)
            key, value = m.group(2), m.group(3)
            if key == "PROPERTY":
                value = value.split(" ", 1)
                value.append("")
                key, value = value[0], value[1]
            self.attr.update(**{key.lower(): value})
            return True
        return False


class Markdown(Reader):
    content_type = Article.CONTENT_TYPE_MARKDOWN

    def parse(self, line):
        regex = re.compile(r'^(.*): (.*)$')
        if regex.match(line):
            m = regex.match(line)
            key, value = m.group(1), m.group(2)
            self.attr.update(**{key.lower(): value})
            return True
        return False


def org_to_db(path):
    files = [
        os.path.join(path, f) for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f)) and f.endswith(".org")
    ]
    articles = []
    for f in files:
        articles.append(Org(f).run())
    return articles


def markdown_to_db(path):
    files = [
        os.path.join(path, f) for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f)) and f.endswith(".md")
    ]
    articles = []
    for f in files:
        articles.append(Markdown(f).run())
    return articles


def main():
    articles = org_to_db("/home/jianglin/git/pelican/content/org")
    articles1 = markdown_to_db("/home/jianglin/git/pelican/content/markdown")

    articles.extend(articles1)

    for article in sorted(articles, key=lambda i: i['date']):
        print(article["title"])
        add_article(**article)


if __name__ == '__main__':
    main()
