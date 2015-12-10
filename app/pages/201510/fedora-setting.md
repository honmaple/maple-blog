Title: fedora安装后设置 
Author: honmaple 
Date: 2015-10-15
Category: linux
Tags: [ linux,fedora ]
Slug: fedora-setting
Summary: 记录一下，省得每次重装都要找（绝大多数转自网络)<br /><br />fedora22 发布后 dnf 代替了 yum

## 1.增加sudo用户组
    $ su  

转到root用户，输入密码  

    # visudo

在root ALL=(ALL) ALL下增加一行  

    yourname ALL=(ALL) ALL  

如果不想每次输入密码更改为  

    yourname ALL=(ALL) NOPASSWD:ALL  

    :wq #保存退出  
    exit #回到一般用户  

## 2.备份的主题，图标,字体拷贝到home目录

    $ cp -r files ~/.theme 
    $ cp -r files ~/.icons
    $ cp -r files ~/.fonts
    $ sudo chmod -R 755 files  

 ## 3. 启用RPM Fusion仓库

    $ sudo rpm -Uhv http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-22.noarch.rpm
    $ sudo rpm -Uhv http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-22.noarch.rpm

## 4.使用 dnf 缓存与dnf 最快源

    # vim /etc/dnf/dnf.conf

添加 keepcache=true 与 fastestmirror=true

## 5. 安装Flash播放器
**32位系统**

    $ sudo rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-i386-1.0-1.noarch.rpm
    $ sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
    $ sudo dnf install flash-plugin


**64位系统**

    $ sudo rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
    $ sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
    $ sudo dnf install flash-plugin


## 6.安装解压缩插件

    $ sudo yum install unrar unzip p7zip


## 7.安装gcc 和g++

    $ sudo yum install gcc gcc-c++

## 8.安装播放器
vlc视频播放器

    $ sudo yum install vlc mplayer

音乐播放器 

    $ sudo yum install moc

歌词  

    osdlyrics

## 9.安装火狐

    $ sudo yum install firefox


## 10.安装code::blocks

    $ sudo yum install codeblocks

## 11.开机默认进文本模式

    $ sudo rm /etc/systemd/system/default.target
    $ sudo ln -sf /lib/systemd/system/multi-user.target /etc/systemd/system/default.target  #文本模式
    $ sudo ln -sf /lib/systemd/system/graphical.target /etc/systemd/system/default.target   #图形模式

## 12.安装头文件

    $ sudo yum install kernel-headers kernel-devel

## 13.一些必要的编译工具

    $ sudo yum install cscope ctags pylint cmake clang gtk2-devel ncurses ncurses-devel

## 14.游戏

    $ sudo yum install asciiquarium sl fortune oneko

    gnome-mines    扫雷  
    gnome-sudoku   数独  
    gnome-mahjongg 对对碰

## 15.输入法

    $ sudo yum install fcitx fcitx-configtool fcitx-qt fcitx-sunpinyin

## 16.联网程序

    $ sudo yum install w3m w3m-img bcloud uget git wget firefox google-chrome-stable

## 17.系统清理

    $ sudo yum install bleachbit

## 18.图像与文字

    $ sudo yum install wps gimp shotwell

## 19.其他

    # vim /etc/sysconfig/selinux  #selinux配置位置
    # vim /etc/sysconfig/iptables  #防火墙配置位置

