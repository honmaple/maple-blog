Title: fedora22成功安装bumblebee-nvidia
Author: honmaple 
Date: 2015-10-15
Category: linux 
Tags: [ linux,fedora,nvidia ]
Slug: bumvlebee
Summary: 参考fedora安装[bumblebee官方wiki](http://fedoraproject.org/wiki/Bumblebee#Description) <br />写在前面：安装前最好更新系统，安装内核头文件等，如果有多余旧内核先删除 <br />安装驱动最好进入字符界面操作


有一些错误，现更正
 
### 将selinux设置为disabled 

    # vim /etc/sysconfig/selinux 
### 安装及必要的依赖

    # dnf install -y libbsd-devel libbsd glibc-devel libX11-devel help2man autoconf git tar glib2 glib2-devel kernel-devel kernel-headers automake gcc gtk2-devel 
    # dnf install VirtualGL 
    # dnf install VirtualGL.i686  # 即使是在64位操作系统上，这个也是必装的
    # dnf -y install http://install.linux.ncsu.edu/pub/yum/itecs/public/bumblebee/fedora22/noarch/bumblebee-release-1.2-1.noarch.rpm 
    # dnf -y install bbswitch bumblebee 
    # dnf -y install http://install.linux.ncsu.edu/pub/yum/itecs/public/bumblebee-nonfree/fedora22/noarch/bumblebee-nonfree-release-1.2-1.noarch.rpm 
    # dnf -y install bumblebee-nvidia 

### 安装完成后加入用户组 

    $ sudo usermod -a -G video username 
    $ sudo usermod -a -G bumblebee username   #username是用户名

### 启动必要服务

    $ sudo systemctl enable dkms 
    $ sudo systemctl enable bumblebeed 
### 重启
    $ reboot 
### 测试bumblebee 
    $ optirun glxgears -info | grep "GL_VENDOR" 
