Title: 使用pelican搭建个人博客
Author: honmaple 
Date: 2015-10-15
Category: python
Tags: [ python,pelican ]
Slug: pelican
Summary: 使用pelican搭建个人博客

## pelican介绍
Pelican是一个用Python语言编写的静态网站生成器，支持使用restructuredText和Markdown写文章，配置灵活，扩展性强  

## pelican安装
```
$ sudo pip install pelican
```
安装markdown
```
$ sudo pip install markdown
```

## pelican使用
工具准备好了，接下来就开始使用
```
$ cd git
$ mkdir pelican  #建立一个文件夹(位置和名称随意，自己记得就行)
$ cd pelican
$ pelican-quickstart
```
显示  (也可以直接回车默认)
```
Welcome to pelican-quickstart v3.4.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? HonMaple
> Who will be the author of this web site? honmaple
> What will be the default language of this web site? [en] zh
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
> What is your URL prefix? (see above example; no trailing slash) http://honmaple.github.io
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using FTP? (y/N)
> Do you want to upload your website using SSH? (y/N)
> Do you want to upload your website using Dropbox? (y/N)
> Do you want to upload your website using S3? (y/N)
> Do you want to upload your website using Rackspace Cloud Files? (y/N)
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
Done. Your new project is available at /home/git/pelican
```
接下来要设置pelicanconf.py和publishconf.py  
具体可以看[官方帮助文档](https://pelican.readthedocs.org/en/latest/)或者参考[我的配置](https://github.com/honmaple/honmaple/)

查看目录  
pelican/  
├── content  
├── output  
├── develop_server.sh  
├── fabfile.py  
├── Makefile  
├── pelicanconf.py       # Main settings file  
└── publishconf.py       # Settings to use when ready to publish  

现在可以开始写第一篇文章了
```
$ cd content
$ mkdir articles pages extra impages
$ cd articles
$ vim hello.md
```
在文件开头输入下列内容
```
Title: 文章标题
Author: 作者 
Date: 2015-10-15
Category: 文章类别
Tags: 标签
Summary: 概要内容

具体内容
```
保存退出后输入
```
$ cd ../../ #进入pelican文件夹下
$ make html
```
可以看实际效果
```
$ google-chrome-stable output/index.html
```
## 提交内容
编辑好内容并且`make html`后需要将内容push到github
```
$ cd output/
$ git init
$ git remote add origin git@github.com:honmaple/honmaple.github.io.git #关联远程仓库
$ git add *
$ git commit -m "My first blog by pelican"
```
过几分钟后就可以看到内容了
