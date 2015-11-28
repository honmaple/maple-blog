#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: email.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-27 21:59:02
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask.ext.mail import Message
from app import mail

def email_send(to,template):
    subject = "Please confirm your email"
    msg = Message(subject,
                  recipients=[to],
                  html=template,
                  sender="1171501218@qq.com")
    mail.send(msg)
