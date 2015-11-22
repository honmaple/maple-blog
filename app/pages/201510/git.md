Title: git学习 
Author: honmaple 
Date: 2015-10-15
Category: linux
Tags: [ linux,git ]
Slug: git
Summary:  

参考资料
[廖雪峰Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)  
记忆一下主要内容：
### 安装git  
```
$ sudo dnf install git
```

### 安装后配置
```
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

### 创建版本库
```
$ mkdir git
$ cd git
$ mkdir "目录名"
$ cd "目录名"
$ git init #将该目录变成可用于git管理的仓库
```

### git操作指令
```
$ git add filename #将文件添加到仓库
$ git commit -m "注释内容"  #将文件提交到仓库，-m后面是本次提交的内容说明
$ git add file1.txt
$ git add file2.txt file3.txt
$ git commit -m "add 3 files." #git commit 可以一次性提交多个文件

$ git status #查看仓库当前状态
$ git diff filename #查看文件修改状态
$ git log --pretty=oneline #查看提交日志
$ git reset --hard HEAD^ #从当前状态回退到上个版本状态 ，上上版本HEAD^^,100个上版本HEAD~100
$ git diff HEAD -- filename #查看工作区与版本库里的最新版本的区别
$ git checkout -- filename #让工作区文件回退到上次提交状态
$ git reset HEAD readme.txt #把暂存区的修改撤销掉
$ git rm filename #删除仓库文件
```

### 远程仓库
```
$ ssh-keygen -t rsa -C"youremail@example.com" #生成公钥与私钥
```
将公钥上传到到[GitHub](https://github/com)账户  
**保存好私钥**

```
$ git remote add origin git@github.com:honmaple/vim.git #关联远程仓库
$ git push -u origin master #把本地库内容推送到远程库
$ git push origin master #以后提交本地内容只要输入这个命令就行
$ git clone git@github.com：honmaple/honmaple.git #从远程库克隆到本地
```
***我这里出现问题(远程的commit比本地的commit要新),需要***
```
$ git pull origin master
```





