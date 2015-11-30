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
from threading import Thread
from app import app
from app import mail

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def email_send(to,template):
    subject = "Please confirm your email"
    msg = Message(subject,
                  recipients=[to],
                  html=template)
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return "OK"
