#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: token.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 21:24:03
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from itsdangerous import URLSafeTimedSerializer
import re
from flask import current_app



def email_token(email):
    config = current_app.config
    print(config['SECRET_KEY'])
    serializer = URLSafeTimedSerializer(config['SECRET_KEY'])
    token = serializer.dumps(email,salt=config['SECURITY_PASSWORD_SALT'])
    return token

def confirm_token(token, expiration=3600):
    config = current_app.config
    serializer = URLSafeTimedSerializer(config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt = config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email

def email_validate(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False
