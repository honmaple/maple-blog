Title: linux的一些操作命令
Author: honmaple 
Date: 2015-10-15
Category: linux
Tags: [ linux ]
Slug: linuxcommand
Summary: 一些linux下的基本操作命令，linux下命令太多，不可能完全记住，记个笔记还是有必要的

### 命令行快捷操作
`ctrl + 左右键`:在单词间跳转  
`ctrl+a`:跳到本行的行首  
`ctrl+e`:跳到页尾  
`Ctrl+u`：删除当前光标前面的文字  
`ctrl+k`：删除当前光标后面的文字  
`Ctrl+L`：进行清屏操作  
`Ctrl+y`:进行恢复删除做  
`Ctrl+w`:删除光标前面的单词的字符  
`Alt – d` ：由光标位置开始，往右删除单词。往行尾删  

### 字符界面播放ascii视频
```
$ mplayer -vo caca MovieName
```

### 打开nvidia设置
```
$ optirun nvidia-settings -c :8
```

### 更新google禁用 GPG 签名检查
```
$ sudo dnf update google-chrome-stable* --nogpgcheck
```

### 字符界面使用鼠标
```
$ sudo dnf install gpm
$ sudo service gpm start
```

### 新字体安装  
字体目录下运行
```
$ mkfontscale
$ mkfontdir
$ fc-cache -fv
```

### ssh代理
```
$ ssh -qTfnN -D 7070 ~@~
```

### 安装vimdoc

`./vimcdoc.sh -i` 安装

`./vimcdoc.sh -u` 卸载

### 编译Youcompleteme
```
$ ./install.sh --clang-completer
```

### vim安装bundle插件管理
```
$ git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
```

