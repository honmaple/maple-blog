Title: postgresql学习1——安装
Author: honmaple 
Date: 2015-11-24
Category: linux
Tags: [sql,postgresql,linux]
Slug: postgresql.md
Summary: 最近从sqlite转到postgresql,虽然postgresql比sqlite更加复杂


### archlinux
[参考资料](https://wiki.archlinux.org/index.php/PostgreSQL)

    $ sudo pacman -S postgresql
    $ sudo mkdir /var/lib/postgres/data #如果已存在则可以不建立
    $ sudo chmod -R postgres:postgres /var/lib/postgres/data
    由于我安装系统时没有生成en_US_UTF-8本地化文件(如果已经生成了的就
    不必再生成)
    $ sudo vim /etc/locale.gen #找到en_US_UTF-8，注释掉
    $ locale-gen

    然后运行
    $ sudo -i -u postgres #或者使用root账户su - postgres
    $ initdb --locale en_US.UTF-8 -E UTF8 -D '/var/lib/postgres/data'
    $ createuser -i #输入你的账户名称,并给管理员权限
    
    最好给postgres用户设置密码
    (注意不是linux系统帐号)
    # su - postgres
    $ psql
    >ALTER USER postgres WITH PASSWORD 'yourpasswd';
     
### centos
[ 参考资料](https://wiki.postgresql.org/wiki/YUM_Installation)

到[这里](http://yum.postgresql.org/)
下载所需要的rpm安装包  
或者直接  

    # yum localinstall http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-centos94-9.4-1.noarch.rpm
    # yum list postgres*
    # yum install postgresql94-server
    # yum install postgresql94-contrib

    # service postgresql initdb  #初始化数据库
    # service postgresql start #启动数据库
    # chkconfig postgresql on  #将数据库服务加入启动列表
    修改PostgreSQL 数据库用户postgres的密码
    (注意不是linux系统帐号)
    # su - postgres
    $ psql
    >ALTER USER postgres WITH PASSWORD 'yourpasswd';

