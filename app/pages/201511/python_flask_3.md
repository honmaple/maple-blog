Title: flask学习笔记——3 
Author: honmaple 
Date: 2015-11-04
Category: python
Tags: [ python,flask ]
Slug: python_flask_3
Summary : 好久没有写东西的，主要是最近在用flask写一个网站，由于写前端界面时为了让UI好看一点，搞得自己晕头转向，方向都错了

好久没有写东西的，主要是最近在用flask写一个网站，由于写前端界面时为了让UI好看一点，搞得自己晕头转向，方向都错了,
在此期间也遇到很多问题，虽然绝大部分已经解决了，但是还有很多没有解决。其实，做一个项目是最能检验能力的。  

     
## 中文网站链接编码
如果访问一个含中文字符的网站，很大可能会提示错误

    import urllib
    urllib.parse.quote(url)
