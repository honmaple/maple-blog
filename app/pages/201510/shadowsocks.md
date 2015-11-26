Title: centos搭建shadowsocks服务端 
Author: honmaple 
Date: 2015-10-15
Category: linux
Tags: [ linux,centos,shadowsocks ]
Slug: shadowsocks
Summary: 刚搭建好，记录下来，用的是centos

## 1.安装必要组建
    # yum install build-essential autoconf libtool openssl-devel gcc -y

## 2.安装git
    # yum install git -y 
    # git --version #安装完后查看版本

## 3.下载shadowsocks-libev源码包并且编译安装
    $ git clone https://github.com/madeye/shadowsocks-libev.git
    $ cd shadowsocks-libev
    $ ./configure 
    # make && make install

##.配置shadowsocks
    # nohup /usr/local/bin/ss-server -s IP地址 -p 端口 -k 密码 -m 加密方式 &

注：*ip地址为当前服务器ip，端口随意，加密方式建议为aes-256-cfb*
## 5.加入开机启动
    # echo "nohup /usr/local/bin/ss-server -s IP地址 -p 端口 -k 密码 -m 加密方式 &" >> /etc/rc.local

## 6.加入防火墙
    # vim /etc/sysconfig/iptables

增加  
`-A INPUT -m state --state NEW -m tcp -p tcp --dport 端口 -j ACCEPT`  
重启防火墙  

    # service iptables restart

## 7.客户端配置
[下载地址](http://https://github.com/librehat/shadowsocks-qt5/wiki/)  
注：如果<http://sourceforge.net/>进不去可以<http://sourceforge.jp>  
*客户端中两个端口，一个是服务端（自己设的端口)
，另一个本地端口（默认1080），配置完成启用系统代理，并且选PAC模式*

----------------
***ok，就这样***

