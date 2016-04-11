#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: botton.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-02-03 16:10:00
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from werkzeug.utils import escape
from wtforms import Field
from wtforms.widgets import HTMLString, html_params


class ButtonWidget(object):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('value', field.value)
        kwargs.setdefault('name', field.name)
        kwargs.setdefault('type',"button")
        return HTMLString('<button %s>%s</button>' % (html_params(**kwargs), escape(field._value())))

class ButtonButtonField(Field):
    widget = ButtonWidget()

    def __init__(self,text,value=None,**kwargs):
        super(ButtonButtonField, self).__init__(**kwargs)
        self.text = text
        self.value = self.name

    def _value(self):
        return str(self.text)
