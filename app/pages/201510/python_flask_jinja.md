Title: flask学习--jinja模板 
Author: honmaple 
Date: 2015-10-24
Category: python
Tags: [ python,flask,jinja ]
Slug: python_flask_jinja.md
Summary: janja2是flask的默认模板,使用模板能够很大程度的将前端与后端分离<br /> 下面内容主要参考

## jinja介绍
Jinja是flask的默认模板引擎。
## jinja设置
+ 在扩展名为 .html 、 .htm 、 .xml 和 .xhtml 的模板中开启自动 转义。
+ 在模板中可以使用 {% autoescape %} 来手动设置是否转义。
+ Flask 在 Jinja2 环境中加入一些全局函数和辅助对象，以增强模板的功能。
