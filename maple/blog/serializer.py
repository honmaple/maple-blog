#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: serializer.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-05 16:13:44 (CST)
# Last Update:星期六 2016-11-5 17:14:58 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.serializer import Serializer
from maple.user.serializer import UserSerializer
from .models import Blog, Tags, Category, Comment


class TagSerializer(Serializer):
    class Meta:
        model = Tags
        fields = ['id', 'name']


class CategorySerializer(Serializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BlogSerializer(Serializer):
    tags = TagSerializer
    category = CategorySerializer
    author = UserSerializer

    class Meta:
        model = Blog
        fields = ['id', 'tags', 'category', 'title', 'content', 'is_copy',
                  'author', 'created_at', 'updated_at']


class CommentSerializer(Serializer):
    author = UserSerializer

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'author']
