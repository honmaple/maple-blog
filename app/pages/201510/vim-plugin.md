Title: 一些vim插件的使用方法
Author: honmaple 
Date: 2015-10-19
Category: linux
Tags: [ linux,vim ]
Slug: vim-plugin
Summary: 关于一些vim插件的使用方法，vim插件多，快捷键也多，记录一下

## tpope/vim-surround
光标在

    "Hello world!"
中时按下 cs"' ，则会替换双引号为单引号：

    'Hello world!' 
继续按下 cs'<q> ，则会替换单引号为 标签

    <q>Hello world!</q>
按下 cst" ，则回到初始的双引号：

     "Hello world!"
要删除符号，则按下 ds"

    Hello world!
当光标在hello上时，按下 ysiw] ，则会变为

    [Hello] world!
这个操作为其加上了包围符号。

### 总结：

1.删除包围符号的命令是 ds ,后面加的字符表示要删除的符号。比如：
>"Hello *world!"           ds"         Hello world!  

2.替换包围符号的命令是 cs ,命令后跟两个参数，分别是被替换的符号和需要使用的符号。比如
>"Hello *world!"           cs"'        'Hello world!'  

3.添加包围符号的命令是 ys ，命令后同样跟两个参数，第一个是一个vim“动作”（motion）或者是一个文本对象。（motion即vim动作，比如说 w 向后一个单词。文本对象简单的来说主要是来通过一些分隔符来标识一段文本，比如 iw 就是一个文本对象，即光标下的单词。）
>  Hello w*orld!             ysiw)       Hello (world)!  

*另外： yss 命令可以用于整行操作，忽略中间的空格。 yS 和 ySS 还能让包围内容单独一行并且加上缩进。*  

4.添加包围符号还有个非常好用的：在可视模式v下，按下 S 后即可添加想要添加的包围符号了。
再说一个小技巧：在包围符号为括时，输入左括号 (或者{ ,则会留一个空格
>Hello w*orld!             ysiw(       Hello ( world )!


