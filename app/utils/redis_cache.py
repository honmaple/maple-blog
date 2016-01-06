#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: redis.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-01-06 21:59:34
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
import redis
import psycopg2
r = redis.StrictRedis(host='localhost', port=6379, db=0)

conn = psycopg2.connect(database="articledb", \
                        user="postgres", \
                        password="qaz123", \
                        host="127.0.0.1", \
                        port="5432")
article = conn.cursor()
article.execute("select id from articles")
rows = article.fetchall()
for row in rows:
    r.set("visit:%s:total"%row[0],0)
    print(row[0])
conn.close()
