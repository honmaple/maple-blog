#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: mark_online.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-01-07 21:04:12
# *************************************************************************
from maple.extensions import redis_data


def get_article_count(article_id):
    '''获取文章阅读次数'''
    article_count = redis_data.zscore("visited:article",
                                      "article:%s" % str(article_id))
    if article_count is None:
        article_count = 0.0
    article_count = int(article_count)
    return article_count
