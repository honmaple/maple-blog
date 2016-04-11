#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: mark_online.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-01-07 21:04:12
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from time import time
from datetime import datetime
from maple import redis_data
from flask import current_app

def get_article_count(article_id):
    '''获取文章阅读次数'''
    article_count = redis_data.zscore("visited:article",
                                      "article:%s"%str(article_id))
    if article_count is None:
        article_count = 0.0
    article_count = int(article_count)
    return article_count

def mark_visited(user_ip,page_name):
    '''记录访问过的用户操作'''
    pipe = redis_data.pipeline()
    visited_users = 'visited_users:%s' % user_ip
    visited_pages = 'visited_pages:%s' % page_name
    '''访问过的用户'''
    pipe.sadd('visited:users',user_ip)
    '''实时查询'''
    page_count = redis_data.zscore(visited_users,visited_pages)
    '''记录访问某个页面的次数'''
    if page_count is None:
        page_count = 1
        pipe.zadd(visited_users,page_count,visited_pages)
    redis_data.zincrby(visited_users,visited_pages,1)
    '''记录访问的时间'''
    now_time = int(time())
    query_last_time = redis_data.zscore(visited_users,'last_time')
    query_now_time = redis_data.zscore(visited_users,'time')
    if query_last_time is None:
        query_last_time = now_time
        pipe.zadd(visited_users,query_last_time,'last_time')
    if query_now_time is None:
        query_now_time = now_time
    '''十分钟'''
    if now_time - query_last_time >= 600:
        pipe.zadd(visited_users,query_now_time,'last_time')
        pipe.zadd(visited_users,now_time,'time')
    else:
        pipe.zadd(visited_users,now_time,'time')
    pipe.expire('visited:users',604800)
    pipe.expire(visited_users,259200)
    pipe.execute()

def get_visited_users():
    '''得到访问用户的信息'''
    visited_users = redis_data.smembers('visited:users')
    return visited_users

def get_visited_time(user_ip):
    '''得到访问时间'''
    visited_users = 'visited_users:%s' % user_ip
    visited_time = redis_data.zscore(visited_users,'time')
    if visited_time is None:
        visited_time = time()
    return datetime.utcfromtimestamp(int(visited_time))

def get_visited_last_time(user_ip):
    '''得到上次访问时间'''
    visited_users = 'visited_users:%s' % user_ip
    visited_last_time = redis_data.zscore(visited_users,'last_time')
    if visited_last_time is None:
        visited_last_time = time()
    return datetime.utcfromtimestamp(int(visited_last_time))

def get_visited_pages(user_ip):
    '''得到访问的页面'''
    visited_users = 'visited_users:%s' % user_ip
    visited_pages = redis_data.zrange(visited_users,0,-1)
    pages = []
    count = []
    for page in visited_pages:
        if ':' in page.decode():
            '''得到访问的页面的次数'''
            visited_count = redis_data.zscore(visited_users,page)
            count.append(int(visited_count))
            p = page.decode()
            p = p.split(':',1)
            pages.append(p[1])
        else:
            pass
    return pages,count

def delete_visited_users(user_ip):
    '''删除访问记录'''
    visited_users = 'visited_users:%s' % user_ip
    redis_data.srem('visited:users',user_ip)
    redis_data.delete(visited_users)

def delete_visited_pages(user_ip):
    '''删除访问页面'''
    visited_users = 'visited_users:%s' % user_ip
    visited_pages = redis_data.zrange(visited_users,0,-1)
    for page in visited_pages:
        if ':' in page.decode():
            redis_data.zrem(visited_users,page)

def mark_online(user_ip):
    '''记录在线用户'''
    config = current_app.config
    now = int(time())
    expires = now + (config['ONLINE_LAST_MINUTES'] * 60) + 10
    online_users_key = 'online_users:%d' % (now // 60)
    user_key = 'user_activity:%s' % user_ip
    p = redis_data.pipeline()
    p.sadd(online_users_key, user_ip)
    p.set(user_key, now)
    p.expireat(online_users_key, expires)
    p.expireat(user_key, expires)
    p.execute()

def get_user_last_activity(user_ip):
    last_active = redis_data.get('user_activity:%s' % user_ip)
    if last_active is None:
        last_active = time()
    return datetime.utcfromtimestamp(int(last_active))

def get_online_users():
    config = current_app.config
    current = int(time()) // 60
    minutes = range(config['ONLINE_LAST_MINUTES'])
    return redis_data.sunion(['online_users:%d' % (current - x)
                         for x in minutes])
