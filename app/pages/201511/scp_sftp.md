Title: 如何上传文件到服务器
Author: honmaple 
Date: 2015-11-26
Category: linux 
Tags: [linux,vps]
Slug: scp_sftp.md
Summary: 主要介绍通过scp和sftp上传文件到服务器，或者从服务器下载文件到本地,其主要命令

## scp介绍
SCP的全称是secure copy (remote file copy program)，此命令是openssh-clients附带
的,它的作用就是在机器之间实现拷贝，且机器之间的传输完全是加密的。

## scp简单操作
    $ scp 帐号@主机:path/filename path/ #从服务器下载文件到本地
    $ scp path/filename 帐号@主机:path/  #上传文件到服务器指定文件夹

>选项与参数：  
-p ：保留原本档案的权限数据；  
-r ：复制来源为目录时，可以复制整个目录 (含子目录)  
-l ：可以限制传输的速度，单位为 Kb/s ，例如 [-l 100] 代表传输速限 100Kb/s

## scp实例
    $ scp /home/xxx/test.md xxx@xxxx:~/ #在使用本地~/目录时，使用tab自动补全会转化为绝对路径
    test.md                                       100%   86     0.1KB/s   00:00
    $ scp xxxx@xxxx:~/test.md /home/xxxx/web/
    test.md                                       100%   86     0.1KB/s   00:00  

可以ssh到服务器查看是否有test.md文件,如果有那就成功了

# sftp
## sftp介绍
sftp是Secure File Transfer Protocol的缩写，安全文件传送协议。可以为传输文件提供
一种安全的加密方法。sftp 与 ftp 有着几乎一样的语法和功能。SFTP 为 SSH的一部分，
是一种传输档案至 Blogger 伺服器的安全方式。其实在SSH软件包中，已经包含了一个叫
作SFTP(Secure File Transfer Protocol)的安全文件传输子系统，SFTP本身没有单独的
守护进程，它必须使用sshd守护进程（端口号默认是22）来完成相应的连接操作，所以从
某种意义上来说，SFTP并不像一个服务器程序，而更像是一个客户端程序。SFTP同样是使
用加密传输认证信息和传输的数据，所以，使用SFTP是非常安全的。但是，由于这种传输
方式使用了加密/解密技术，所以传输效率比普通的FTP要低得多，如果您对网络安全性要
求更高时，可以使用SFTP代替FTP。

## sftp基本操作
    $ sftp xxxx@xxxx  #类似ssh登陆
    Connected to xxxx
    sftp> 

针对服务器  

    sftp>cd /home/xxx/test/ 切换目录
    sftp>ls   #就是一些linux上的基本操作(ls mkdir chown rm mv)
    sftp>pwd  #显示目前所在的目录
    sftp>exit #退出

针对本地  

    sftp>lcd /home/xxx/test/
    sftp>lls #在基本命令前加l(L小写l)
    sftp>lpwd  #显示目前所在的目录
    sftp>exit #退出

## 上传下载文件
上传  

    $ put ~/test.md /home/xxx/test/ # 将本机的test.md文件上传到服务器

下载  

    $ get /home/xxx/test/test.md ~/web/ #将服务器上的test.md下载到本地


这些命令对我来说就足够了，如果你还有其他要求**man**是最好的伙伴
