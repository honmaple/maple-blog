Title: postgresql学习
Author: honmaple 
Date: 2015-11-24
Category: linux
Tags: [sql,postgresql,linux]
Slug: postgresql.md
Summary: 最近从sqlite转到postgresql


## postgresql安装
### archlinux
    $ sudo pacman -S postgresql
    $ sudo mkdir /var/lib/postgres/data #如果已存在则可以不建立
    由于安装系统时没有安装en_US_UTF-8,所以
    $ sudo vim /etc/locale.gen #找到en_US_UTF-8，注释掉
    $ locale-gen
    然后运行
    $ sudo -i -u postgres
    $ initdb --
    $ sudo chmod -R postgres:postgres /var/lib/postgres/data
    
    $ createuser -i #输入你的账户名称,并给管理员权限
     
### centos
添加源

