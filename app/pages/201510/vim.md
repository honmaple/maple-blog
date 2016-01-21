Title: vim配置  
Author: honmaple   
Date: 2015-10-15
Category: linux  
Tags: [ vim,linux ]  
Slug: vim  
Summary: vim号称编辑器之神，最近也一直使用vim写代码，最大的印象就是快，无论是临时修改文件，还是专门写代码.现在记录vim主要操作快捷键和我的vim配置   
  

# vim操作  
## 一、移动光标  
1.左移h、右移l、下移j、上移k    
2.向下翻页ctrl + f，向上翻页ctrl + b  
3.向下翻半页ctrl + d，向上翻半页ctrl + u  
4.移动到行尾$，移动到行首0（数字），移动到行首第一个字符处^  
5.移动光标到下一个句子 ），移动光标到上一个句子（  
6.移动到段首{，移动到段尾}  
7.移动到下一个词w，移动到上一个词b  
8.移动到文档开始gg，移动到文档结束G  
9.移动到匹配的{}.().[]处%  
10、跳到第n行 ngg 或 nG 或 :n  
11、移动光标到屏幕顶端H，移动到屏幕中间M，移动到底部L  
12、读取当前字符，并移动到本屏幕内下一次出现的地方 *  
13、读取当前字符，并移动到本屏幕内上一次出现的地方 #  
  
  
## 二、查找替换  
  
1.光标向后查找关键字 #或者g#  
2.光标向前查找关键字 *或者g*  
3.当前行查找字符 fx, Fx, tx, Tx  
4.基本替换 :s/s1/s2 （将下一个s1替换为s2）  
5.全部替换 :%s/s1/s2  
6.只替换当前行 :s/s1/s2/g  
7.替换某些行 :n1,n2 s/s1/s2/g  
8.搜索模式为 /string，搜索下一处为n，搜索上一处为N  
9.制定书签 mx, 但是看不到书签标记，而且只能用小写字母  
10.移动到某标签处 \`x，1旁边的键  
11.移动到上次编辑文件的位置 \`.  
>PS：.代表一个任意字符 *代表一个或多个字符的重复  
  
## 三、编辑操作  
1.光标后插入a, 行尾插入A  
2.后插一行插入o，前插一行插入O  
3.删除字符插入s， 删除正行插入S  
4.光标前插入i，行首插入I  
5.删除一行dd，删除后进入插入模式cc或者S  
6.删除一个单词dw，删除一个单词进入插入模式cw  
7.删除一个字符x或者dl，删除一个字符进入插入模式s或者cl  
8.粘贴p，交换两个字符xp，交换两行ddp  
9.复制y，复制一行yy  
10.撤销u，重做ctrl + r，重复.  
11.智能提示 ctrl + n 或者 ctrl + p  
12.删除motion跨过的字符，删除并进入插入模式 c{motion}  
13.删除到下一个字符跨过的字符，删除并进入插入模式，不包括x字符 ctx  
14.删除当前字符到下一个字符处的所有字符，并进入插入模式，包括x字符，cfx  
15.删除motion跨过的字符，删除但不进入插入模式 d{motion}  
16.删除motion跨过的字符，删除但不进入插入模式，不包括x字符 dtx  
17.删除当前字符到下一个字符处的所有字符，包括x字符 dfx  
18.如果只是复制的情况时，将12-17条中的c或d改为y  
19.删除到行尾可以使用D或C  
20.拷贝当前行 yy或者Y  
21.删除当前字符 x  
22.粘贴 p  
23.可以使用多重剪切板，查看状态使用:reg，使用剪切板使用”，例如复制到w寄存器，”wyy，或者使用可视模式v”wy  
24.重复执行上一个作用使用.  
25.使用数字可以跨过n个区域，如y3x，会拷贝光标到第三个x之间的区域，3j向下移动3行  
26.在编写代码的时候可以使用]p粘贴，这样可以自动进行代码缩进  
27. \>> 缩进所有选择的代码, << 反缩进所有选择的代码  
28.gd 移动到光标所处的函数或变量的定义处  
29.K 在man里搜索光标所在的词  
30.合并两行 J  
31.若不想保存文件，而重新打开 :e!  
32.若想打开新文件 :e filename，然后使用ctrl + ^进行文件切换  

## 四.窗口操作  
1.分隔一个窗口:split或者:vsplit  
2.创建一个窗口:new或者:vnew  
3.在新窗口打开文件:sf {filename}  
4.关闭当前窗口:close  
5.仅保留当前窗口:only  
6.到左边窗口 ctrl + w, h  
7.到右边窗口 ctrl + w, l  
8.到上边窗口 ctrl + w, k  
9.到下边窗口 ctrl + w, j  
10.到顶部窗口 ctrl + w, t  
11.到底部窗口 ctrl + w, b  
  
## 五.宏操作  
1.开始记录宏操作q[a-z]，按q结束，保存操作到寄存器[a-z]中  
2.@[a-z]执行寄存器[a-z]中的操作  
3.@@执行最近一次记录的宏操作  
  
## 六、可视操作  
1.进入块可视模式 ctrl + v  
2.进入字符可视模式 v  
3.进入行可视模式 V  
4.删除选定的块 d  
5.删除选定的块然后进入插入模式 c  
6.在选中的块同是插入相同的字符 I<String>ESC  
  
## 七.跳到声明  
1.[[ 向前跳到顶格第一个{    
2.[] 向前跳到顶格第一个}  
3.]] 向后跳到顶格的第一个{  
4.]] 向后跳到顶格的第一个}  
5.[{ 跳到本代码块的开头  
6.]} 跳到本代码块的结尾  
  
## 八.挂起操作  
1.挂起Vim ctrl + z 或者 :suspend  
2.查看任务 在shell中输入 jobs  
3.恢复任务 fg [job number]（将后台程序放到前台）或者 bg [job number]（将前台程序放到后台）  
4.执行shell命令 :!command  
5.开启shell命令 :shell，退出该shell exit  
6.保存vim状态 :mksession name.vim  
7.恢复vim状态 :source name.vim  
8.启动vim时恢复状态 vim -S name.vim  
  
  
  
  
## vim配置  
[我的vimrc配置](http://github.com/honmaple/vim)  
```  
let g:iswindows = 0  
let g:islinux = 0  
if(has("win32") || has("win64") || has("win95") || has("win16"))  
    let g:iswindows = 1  
else  
    let g:islinux = 1  
endif  
   
" -----------------------------------------------------------------------------  
"  < 判断是终端还是 Gvim >  
" -----------------------------------------------------------------------------  
if has("gui_running")  
    let g:isGUI = 1  
else  
    let g:isGUI = 0  
endif  
  
" -----------------------------------------------------------------------------  
"  < Windows Gvim 配置>  
" -----------------------------------------------------------------------------  
if (g:iswindows && g:isGUI)  
    source $VIMRUNTIME/vimrc_example.vim  
    source $VIMRUNTIME/mswin.vim  
    behave mswin  
    set diffexpr=MyDiff()  
   
    function MyDiff()  
        let opt = '-a --binary '  
        if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif  
        if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif  
        let arg1 = v:fname_in  
        if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif  
        let arg2 = v:fname_new  
        if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif  
        let arg3 = v:fname_out  
        if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif  
        let eq = ''  
        if $VIMRUNTIME =~ ' '  
            if &sh =~ '\<cmd'  
                let cmd = '""' . $VIMRUNTIME . '\diff"'  
                let eq = '"'  
            else  
                let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'  
            endif  
        else  
            let cmd = $VIMRUNTIME . '\diff'  
        endif  
        silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq  
    endfunction  
endif  
   
  
" -----------------------------------------------------------------------------  
"  < Vundle 插件管理工具配置 >  
" -----------------------------------------------------------------------------  
" 用于更方便的管理vim插件，具体用法参考 :h vundle 帮助  
" Vundle工具安装方法为在终端输入如下命令  
" git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle  
" 如果想在 windows 安装就必需先安装 "git for window"，可查阅网上资料  
   
set nocompatible                                      "禁用 Vi 兼容模式  
filetype off                                          "禁用文件类型侦测  
   
  
set rtp+=~/.vim/bundle/vundle/  
call vundle#rc()  
  
   
" 使用Vundle来管理插件，这个必须要有。  
Bundle 'gmarik/vundle'  
" 可以通过以下四种方式指定插件的来源    
" a) 指定Github中vim-scripts仓库中的插件，直接指定插件名称即可，插件明中的  
"   空格使用“-”代替。    
Bundle 'L9'  
Bundle 'FuzzyFinder'  
"       " c) 指定非Github的Git仓库的插件，需要使用git地址    
Bundle 'git://git.wincent.com/command-t.git'    
   
" 以下为要安装或更新的插件，不同仓库都有（具体书写规范请参考帮助）  
Bundle 'a.vim'  
Bundle 'Align'  
Bundle 'jiangmiao/auto-pairs'  
Bundle 'bufexplorer.zip'  
Bundle 'mattn/emmet-vim'  
Bundle 'Yggdroot/indentLine'  
Bundle 'scrooloose/nerdtree'  
Bundle 'scrooloose/nerdcommenter'  
Bundle 'Lokaltog/vim-powerline'  
Bundle 'bling/vim-bufferline'  
Bundle 'kien/ctrlp.vim'  
Bundle 'tacahiroy/ctrlp-funky'  
Bundle 'repeat.vim'  
Bundle 'wesleyche/SrcExpl'  
Bundle 'scrooloose/syntastic'  
Bundle 'majutsushi/tagbar'  
Bundle 'taglist.vim'  
"Bundle 'TxtBrowser'  
Bundle 'cscope.vim'  
Bundle 'ctags.vim'  
Bundle 'Lokaltog/vim-easymotion'  
"Bundle 'c.vim'  
Bundle 'hallison/vim-markdown'  
Bundle 'winmanager'  
"Bundle 'python_ifold'  
Bundle 'molokai'  
Bundle 'altercation/vim-colors-solarized'  
Bundle 'vimwiki'  
Bundle 'kevinw/pyflakes-vim'  
Bundle 'hdima/python-syntax'  
Bundle 'Valloric/YouCompleteMe'  
Bundle 'SirVer/ultisnips'  
Bundle 'honza/vim-snippets'  
Bundle 'ap/vim-css-color'  
Bundle 'jelera/vim-javascript-syntax'  
Bundle "pangloss/vim-javascript"  
  
" ==========================================  
" javascript插件设置  
" ==========================================  
let g:html_indent_inctags = "html,body,head,tbody"  
let g:html_indent_script1 = "inc"  
let g:html_indent_style1 = "inc"  
  
"===========================================  
"syntastic设置  
"===========================================  
let g:syntastic_error_symbol='>>'  
let g:syntastic_warning_symbol='>'  
let g:syntastic_check_on_open=1  
let g:syntastic_check_on_wq=0  
let g:syntastic_enable_highlighting=1  
"let g:syntastic_python_checkers=['pyflakes'] " 使用pyflakes  
" error code: http://pep8.readthedocs.org/en/latest/intro.html#error-codes  
"let g:syntastic_python_checkers=['pyflakes', 'pep8'] " 使用pyflakes  
"let g:syntastic_python_pep8_args='--ignore=E501,E225'  
let g:syntastic_python_checkers=['pyflakes', 'pylint']  
let g:syntastic_python_checkers=['pylint']  
let g:syntastic_python_pylint_args='--disable=C0111,R0903,C0301'  
  
  
let g:syntastic_javascript_checkers = ['jsl', 'jshint']  
let g:syntastic_html_checkers=['tidy', 'jshint']  
  
" 修改高亮的背景色, 适应主题  
highlight SyntasticErrorSign guifg=white guibg=black  
  
" to see error location list  
let g:syntastic_always_populate_loc_list = 0  
let g:syntastic_auto_loc_list = 0  
let g:syntastic_loc_list_height = 5  
  
  
"===================================================  
"     Youcompleteme自动补全   
"===================================================  
"youcompleteme  默认tab  s-tab 和自动补全冲突  
let g:ycm_key_list_select_completion = ['<Down>']  
let g:ycm_key_list_previous_completion = ['<Up>']  
let g:ycm_complete_in_comments = 1  "在注释输入中也能补全  
let g:ycm_complete_in_strings = 1   "在字符串输入中也能补全  
let g:ycm_use_ultisnips_completer = 1 "提示UltiSnips  
let g:ycm_collect_identifiers_from_comments_and_strings = 1   "注释和字符串中的文字也会被收入补全  
let g:ycm_collect_identifiers_from_tags_files = 1  
let g:ycm_seed_identifiers_with_syntax=1   "语言关键字补全, 不过python关键字都很短，所以，需要的自己打开  
let g:ycm_cache_omnifunc=0 " 禁止缓存匹配项,每次都重新生成匹配项  
  
" 跳转到定义处, 分屏打开  
let g:ycm_goto_buffer_command = 'horizontal-split'  
" nnoremap <leader>jd :YcmCompleter GoToDefinition<CR>  
nnoremap <leader>jd :YcmCompleter GoToDefinitionElseDeclaration<CR>  
nnoremap <leader>gd :YcmCompleter GoToDeclaration<CR>  
  
if !empty(glob("~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py"))  
    let g:ycm_global_ycm_extra_conf = "~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py"  
endif  
  
" YCM 补全菜单配色  
" 菜单  
"highlight Pmenu ctermfg=2 ctermbg=3 guifg=#005f87 guibg=#EEE8D5  
" 选中项  
"highlight PmenuSel ctermfg=2 ctermbg=3 guifg=#AFD700 guibg=#106900  
" 直接触发自动补全 insert模式下  
" let g:ycm_key_invoke_completion = '<C-Space>'  
" 黑名单,不启用  
let g:ycm_filetype_blacklist = {  
      \ 'tagbar' : 1,  
      \ 'gitcommit' : 1,  
      \}  
"===========================================  
"快速插入代码片段  
"===========================================  
"let g:UltiSnipsExpandTrigger = '<C-space>'  
"let g:UltiSnipsJumpForwardTrigger = '<Down>'  
"let g:UltiSnipsJumpBackwardTrigger = '<Up>'  
"定义存放代码片段的文件夹 .vim/snippets下，使用自定义和默认的，将会的到全局，有冲突的会提示  
let g:UltiSnipsSnippetDirectories=['bundle/vim-snippets', 'bundle/ultisnips']  
  
function! g:UltiSnips_Complete()  
    call UltiSnips#ExpandSnippet()  
    if g:ulti_expand_res == 0  
        if pumvisible()  
            return "\<Down>"  
        else  
            call UltiSnips#JumpForwards()  
            if g:ulti_jump_forwards_res == 0  
               return "\<TAB>"  
            endif  
        endif  
    endif  
    return ""  
endfunction  
  
au BufEnter * exec "inoremap <silent> " . g:UltiSnipsExpandTrigger . " <C-R>=g:UltiSnips_Complete()<cr>"  
let g:UltiSnipsJumpForwardTrigger="<tab>"  
let g:UltiSnipsListSnippets="<c-e>"  
"回车即选中当前项  
inoremap <expr> <CR> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"  
if has('conceal')  
    set conceallevel=2 concealcursor=i  
endif  
  
  
" ==========================================  
"  < indentLine 插件配置 >  
" ==========================================  
" 用于显示对齐线，与 indent_guides 在显示方式上不同，根据自己喜好选择了  
" 在终端上会有屏幕刷新的问题，这个问题能解决有更好了  
" 开启/关闭对齐线  
  
let g:indentLine_char = "┊"  
let g:indentLine_first_char = "┊"  
" 色块宽度  
"let g:indent_guides_guide_size=1  
" 设置终端对齐线颜色，如果不喜欢可以将其注释掉采用默认颜色  
let g:indentLine_color_term = 256  
  
" ==========================================  
"    markdown  
" ==========================================  
au BufRead,BufNewFile *.{md,mdown,mkd,mkdn,markdown,mdwn} set filetype=mkd  
let g:vim_markdown_folding_disabled=1  
let g:vim_markdown_no_default_key_mappings=1  
" ==========================================  
" ctrlp  
" =========================================  
let g:ctrlp_working_path_mode = 'ra'  
let g:ctrlp_custom_ignore = {  
    \ 'dir':  '\.git$\|\.hg$\|\.svn$',  
    \ 'file': '\.exe$\|\.so$\|\.dll$\|\.pyc$' }  
let g:ctrlp_working_path_mode=0  
let g:ctrlp_match_window_bottom=1  
let g:ctrlp_max_height=15  
let g:ctrlp_match_window_reversed=0  
let g:ctrlp_mruf_max=500  
let g:ctrlp_follow_symlinks=1  
  
" ==========================================  
" ctrlp-funky  
" ==========================================  
let g:ctrlp_extensions = ['funky']  
let g:ctrlp_funky_syntax_highlight = 1  
  
" ==========================================  
"  < Tagbar 插件配置 >  
" ==========================================  
" 相对 TagList 能更好的支持面向对象  
   
" 常规模式下输入 tb 调用插件，如果有打开 TagList 窗口则先将其关闭  
"nmap tb :TlistClose<CR>:TagbarToggle<CR>  
   
let g:tagbar_width=20                       "设置窗口宽度  
let g:tagbar_left=1                         "在左侧窗口中显示  
let g:tagbar_compact=1                      "不显示帮助信息  
let g:winManagerWindowLayout = "TagList|FileExplorer,BufExplorer"  
"let g:winManagerWindowLayout = "TagList|Tagbar"  
" ===========================================  
"  < TagList 插件配置 >  
" ===========================================  
" 高效地浏览源码, 其功能就像vc中的workpace  
" 那里面列出了当前文件中的所有宏,全局变量, 函数名等  
   
" 常规模式下输入 tl 调用插件，如果有打开 Tagbar 窗口则先将其关闭  
"nmap tl :TagbarClose<CR>:Tlist<CR>  
   
let Tlist_Show_One_File=1                   "只显示当前文件的tags  
let Tlist_Show_Menu=1                       "显示菜单  
let Tlist_Enable_Fold_Column=0              "使taglist插件不显示左边的折叠行  
let Tlist_Exit_OnlyWindow=1                 "如果Taglist窗口是最后一个窗口则退出Vim  
let Tlist_File_Fold_Auto_Close=1            "自动折叠  
let Tlist_WinWidth=20                       "设置窗口宽度  
let Tlist_Use_Right_Window=1                "在右侧窗口中显示  
  
" ===========================================  
"          nerdcommenter  
" ===========================================  
" <leader>cc，注释当前选中文本，如果选中的是整行则在每行首添加 //，如果选中一行的部分内容则在选中部分前后添加分别 / 、 /；  
"<leader>cu，取消选中文本块的注释  
"  
" ===========================================  
"  < txtbrowser 插件配置 >  
" ===========================================  
" 用于文本文件生成标签与与语法高亮（调用TagList插件生成标签，如果可以）  
"au BufRead,BufNewFile *.txt setlocal ft=txt  
  
""""""""""""""""""""""""""""""  
" BufExplorer  
""""""""""""""""""""""""""""""  
"<Leader>be　　全屏方式打来 buffer 列表  
"<Leader>bs　　水平窗口打来 buffer 列表  
"<Leader>bv　　垂直窗口打开 buffer 列表  
"let g:bufExplorerDefaultHelp=0       " Do not show default help.  
"let g:bufExplorerShowRelativePath=1  " Show relative paths.  
"let g:bufExplorerSortBy='mru'        " Sort by most recently used.  
"let g:bufExplorerSplitRight=0        " Split left.  
"let g:bufExplorerSplitVertical=1     " Split vertically.  
"let g:bufExplorerSplitVertSize = 30  " Split width  
"autocmd BufWinEnter \[Buf\ List\] setl nonumber  
"  
"  
" ===========================================  
"  < cscope 工具配置 >  
" ===========================================  
" 用Cscope自己的话说 你可以把它当做是超过频的ctags  
if has("cscope")  
    "设定可以使用 quickfix 窗口来查看 cscope 结果  
    set cscopequickfix=s-,c-,d-,i-,t-,e-  
    "使支持用 Ctrl+]  和 Ctrl+t 快捷键在代码间跳转  
    set cscopetag  
    "如果你想反向搜索顺序设置为1  
    set csto=0  
    "在当前目录中添加任何数据库  
    if filereadable("cscope.out")  
        cs add cscope.out  
    "否则添加数据库环境中所指出的  
    elseif $CSCOPE_DB != ""  
        cs add $CSCOPE_DB  
    endif  
    set cscopeverbose  
    "快捷键设置  
    nmap <C-\>s :cs find s <C-R>=expand("<cword>")<CR><CR>  
    nmap <C-\>g :cs find g <C-R>=expand("<cword>")<CR><CR>  
    nmap <C-\>c :cs find c <C-R>=expand("<cword>")<CR><CR>  
    nmap <C-\>t :cs find t <C-R>=expand("<cword>")<CR><CR>  
    nmap <C-\>e :cs find e <C-R>=expand("<cword>")<CR><CR>  
    nmap <C-\>f :cs find f <C-R>=expand("<cfile>")<CR><CR>  
    nmap <C-\>i :cs find i ^<C-R>=expand("<cfile>")<CR>$<CR>  
    nmap <C-\>d :cs find d <C-R>=expand("<cword>")<CR><CR>  
endif  
   
" =========================================  
"  < ctags 工具配置 >  
" =========================================  
" 对浏览代码非常的方便,可以在函数,变量之间跳转等  
set tags=./tags;                            "向上级目录递归查找tags文件（好像只有在Windows下才有用）  
   
" 自动切换目录为当前编辑文件所在目录  
au BufRead,BufNewFile,BufEnter * cd %:p:h  
  
" =========================================  
" vimwiki设置  
" =========================================  
let g:vimwiki_use_mouse = 1  
let g:vimwiki_list = [{'path': '~/MyCode/vimwiki/',    
  \ 'path_html': '~/MyCode/vimwiki_html/',  
  \ 'html_header': '~/MyCode/vimwiki_template/header.htm',  
  \ 'html_footer': '~/MyCode/vimwiki_template/footer.htm',}]  
    
  
" =========================================  
"NerdTree设置  
" =========================================  
"autocmd BufEnter * :syntax sync fromstart  
"set hid             " 可以在没有保存的情况下切换buffer  
" 自动开启nerdtree  
let g:nerdtree_tabs_open_on_console_startup=1  
  
"当打开vim且没有文件时自动打开NERDTree  
autocmd vimenter * if !argc() | NERDTree | endif  
" 只剩 NERDTree时自动关闭  
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif  
"显示文件  
let NERDTreeShowFiles=1  
"显示隐藏文件  
let NERDTreeShowHidden=0  
"高亮显示当前文件或目录  
let NERDTreeHightCursorline=1  
"不显示'Bookmarks' label 'Press ? for help'  
let NERDTreeMinimalUI=1  
" s/v 分屏打开文件  
let g:NERDTreeMapOpenSplit = 's'  
let g:NERDTreeMapOpenVSplit = 'v'  
  
" =========================================  
" python语法实时检查  
" =========================================  
  
" python fly check, 弥补syntastic只能打开和保存才检查语法的不足  
let g:pyflakes_use_quickfix = 1  
  
" for python.vim syntax highlight  
let python_highlight_all = 1  
  
  
  
  
  
  
   
  
" ========================================  
"  General Settings 基础设置  
" ========================================  
" 修改leader键  
let mapleader = ','  
let g:mapleader = ','  
  
filetype on                    "启用文件类型侦测  
filetype plugin on             "针对不同的文件类型加载对应的插件  
filetype plugin indent on      "启用缩进  
syntax on                      "代码高亮  
"syntax enable  
set t_Co=256  
set background=dark  
if has("gui_running")  
    let g:solarized_termcolors=256  "这个必须在前  
    colorscheme solarized           "终端配色方案  
else  
    let g:molokai_original = 1  
    colorscheme molokai            "终端配色方案  
endif  
"colorscheme solarized           "终端配色方案  
"let g:solarized_termcolors=256  
"let g:solarized_termtrans=1  
"let g:solarized_contrast='normal'  
"let g:solarized_visibility='normal'  
set mouse=a                    "任何模式下启用鼠标  
set mousehide                  "Hide the mouse cursor while typing  
scriptencoding utf-8  
  
if has('clipboard')  
    if has('unnamedplus')  " When possible use + register for copy-paste  
		set clipboard=unnamed,unnamedplus  
    else         " On mac and Windows, use * register for copy-paste  
		set clipboard=unnamed  
    endif  
endif  
  
set shortmess+=filmnrxoOtT          "去掉欢迎界面  
set guifont=Monospace\ 12  
set viewoptions=folds,options,cursor,unix,slash " Better Unix / Windows compatibility  
set virtualedit=onemore             " Allow for cursor beyond last character  
set history=1000                    " Store a ton of history (default is 20)  
"set spell                           "启用拼写检查  
set hidden                          " Allow buffer switching without saving  
set iskeyword-=.                    " '.' is an end of word designator  
set iskeyword-=#                    " '#' is an end of word designator  
set iskeyword-=-                    " '-' is an end of word designator  
  
"set backup                          "设置备份文件  
"if has('persistent_undo')  
"    set undofile                " So is persistent undo ...  
"    set undolevels=1000         " Maximum number of changes that can be undone  
"    set undoreload=10000        " Maximum number lines to save for undo on a buffer reload  
"endif  
  
set tabpagemax=15               " Only show 15 tabs  
set showmode                    " Display the current mode  
  
set cursorline                  "高亮光标所在行  
set cuc                         "高亮光标所在列  
  
highlight clear SignColumn      " SignColumn should match background  
highlight clear LineNr          " Current line number row will have same background color in relative mode  
"highlight clear CursorLineNr    " Remove highlight color from current line number  
  
"if has('cmdline_info')  
"    set ruler                   " Show the ruler  
"    set rulerformat=%30(%=\:b%n%y%m%r%w\ %l,%c%V\ %P%) " A ruler on steroids  
"    set showcmd                 " Show partial commands in status line and  
                                    " Selected characters/lines in visual mode  
"endif  
  
"if has('statusline')  
    set laststatus=2                         "启用状态栏信息  
"    set statusline=%<%f\                     " Filename  
"    set statusline+=%w%h%m%r                 " Options  
"    set statusline+=\ [%{&ff}/%Y]            " Filetype  
"    set statusline+=\ [%{getcwd()}]          " Current dir  
"    set statusline+=%=%-14.(%l,%c%V%)\ %p%%  " Right aligned file nav info  
"endif  
  
set backspace=indent,eol,start  " Backspace for dummies  
set linespace=0                 " No extra spaces between rows  
set number                      "显示行号  
set relativenumber number       "设置相对行号  
au FocusLost * :set norelativenumber number  
au FocusGained * :set relativenumber  
" 插入模式下用绝对行号, 普通模式下用相对  
autocmd InsertEnter * :set norelativenumber number  
autocmd InsertLeave * :set relativenumber  
function! NumberToggle()  
    if(&relativenumber == 1)  
        set norelativenumber number  
    else  
        set relativenumber  
    endif  
endfunc  
set scrolloff=10                  "在上下移动光标时，光标的上方或下方至少会保留显示的行数  
set showmatch                   "高亮显示匹配的括号  
set incsearch                   "在输入要搜索的文字时，实时匹配  
set hlsearch                    "高亮搜索  
"set winminheight=0              " Windows can be 0 line high  
set ignorecase                  "搜索模式里忽略大小写  
set smartcase                   "如果搜索模式包含大写字符，不使用'ignorecase' 选项，只有在输入搜索模式并且打开 'ignorecase' 选项时才会使用  
set wildmenu  
" 增强模式中的命令行自动完成操作  
set wildmode=list:longest,full  " Command <Tab> completion, list matches, then longest common part, then all.  
set whichwrap=b,s,h,l,<,>,[,]   " Backspace and cursor keys wrap too  
"让Vim的补全菜单行为与一般IDE一致(参考VimTip1228)  
set completeopt=longest,menu  
set wildignore=*.o,*~,*.pyc,*.class  
"set scrolljump=5                " Lines to scroll when cursor leaves screen  
"set scrolloff=3                 " Minimum lines to keep above and below cursor  
set foldenable                  "启用折叠  
set list  
set listchars=tab:›\ ,trail:•,extends:#,nbsp:. " Highlight problematic whitespace  
set showcmd                       "在状态栏显示正在输入的命令  
  
set nowrap                      "设置不自动换行  
set autoindent                  "打开自动缩进  
set shiftwidth=4                "换行时自动缩进宽度，可更改（宽度同tabstop）  
set expandtab                   "将Tab键转换为空格  
set tabstop=4                   "设置Tab键的宽度，可以更改，如：宽度为2  
"set softtabstop=4               " Let backspace delete indent  
"set nojoinspaces                " Prevents inserting two spaces after punctuation on a join (J)  
"set splitright                  " Puts new vsplit windows to the right of the current  
"set splitbelow                  " Puts new split windows to the bottom of the current  
"set pastetoggle=<F12>           " pastetoggle (sane indentation on pastes)  
"autocmd BufNewFile,BufRead *.html.twig set filetype=html.twig  
"autocmd FileType haskell,puppet,ruby,yml setlocal expandtab shiftwidth=2 softtabstop=2  
"autocmd BufNewFile,BufRead *.coffee set filetype=coffee  
  
"autocmd FileType haskell setlocal commentstring=--\ %s  
"autocmd FileType haskell,rust setlocal nospell  
  
let g:FoldMethod = 0  
fun! ToggleFold()  
    if g:FoldMethod == 0  
        exe "normal! zM"  
        let g:FoldMethod = 1  
    else  
        exe "normal! zR"  
        let g:FoldMethod = 0  
    endif  
endfun  
  
function! ToggleBG()  
    let s:tbg = &background  
    " Inversion  
    if s:tbg == "dark"  
        set background=light  
    else  
        set background=dark  
    endif  
endfunction  
  
  
"set smartindent                "启用智能对齐方式  
"set shiftround                 "缩进时，取整  
"set showtabline=1              "显示标签  
set smarttab                   "指定按一次backspace就删除shiftwidth宽度  
"set foldmethod=indent          "indent 折叠方式  
set foldmethod=syntax  
"set foldmethod=marker  
" 启动 vim 时关闭折叠代码  
set nofoldenable  
"set matchtime=5                "匹配括号高亮的时间（单位是十分之一秒）  
"set autoread                   "当文件在外部被修改，自动更新该文件  
"set autowrite                  "自动保存  
set vb t_vb=                   "关闭提示音  
   
" 启用每行超过80列的字符提示（字体变蓝并加下划线），不启用就注释掉  
"au BufWinEnter * let w:m2=matchadd('Underlined', '\%>' . 80 . 'v.\+', -1)  
   
" ===============================  
"       < 界面配置 >  
" ===============================  
  
" 显示/隐藏菜单栏、工具栏、滚动条，可用 Ctrl + F11 切换  
if has("gui_running")  
	winpos 100 10                 "指定窗口出现的位置，坐标原点在屏幕左上角  
    set lines=38 columns=120   
    set guioptions-=m  
    set guioptions-=T  
    set guioptions-=r  
    set guioptions-=L  
    nmap <silent> <c-F11> :if &guioptions =~# 'm' <Bar>  
        \set guioptions-=m <Bar>  
        \set guioptions-=T <Bar>  
        \set guioptions-=r <Bar>  
        \set guioptions-=L <Bar>  
    \else <Bar>  
        \set guioptions+=m <Bar>  
        \set guioptions+=T <Bar>  
        \set guioptions+=r <Bar>  
        \set guioptions+=L <Bar>  
    \endif<CR>  
endif  
  
   
  
"==========================================  
" others 其它设置  
"==========================================  
autocmd! bufwritepost _vimrc source % " vimrc文件修改之后自动加载。 windows。  
autocmd! bufwritepost .vimrc source % " vimrc文件修改之后自动加载。 linux。  
  
"离开插入模式后自动关闭预览窗口  
autocmd InsertLeave * if pumvisible() == 0|pclose|endif  
  
if has("autocmd")  
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif  
endif  
  
" Python 文件的一般设置，比如不要 tab 等  
"autocmd FileType python set tabstop=4 shiftwidth=4 expandtab ai  
"autocmd FileType ruby set tabstop=2 shiftwidth=2 softtabstop=2 expandtab ai  
"autocmd BufRead,BufNew *.md,*.mkd,*.markdown  set filetype=markdown.mkd  
  
" 保存python文件时删除多余空格  
fun! <SID>StripTrailingWhitespaces()  
    let l = line(".")  
    let c = col(".")  
    %s/\s\+$//e  
    call cursor(l, c)  
endfun  
autocmd FileType c,cpp,java,go,php,javascript,puppet,python,rust,twig,xml,yml,perl autocmd BufWritePre <buffer> :call <SID>StripTrailingWhitespaces()  
  
"设置标记一列的背景颜色和数字一行颜色一致  
hi! link SignColumn   LineNr  
hi! link ShowMarksHLl DiffAdd  
hi! link ShowMarksHLu DiffChange  
  
" for error highlight，防止错误整行标红导致看不清  
highlight clear SpellBad  
highlight SpellBad term=standout ctermfg=1 term=underline cterm=underline  
highlight clear SpellCap  
highlight SpellCap term=underline cterm=underline  
highlight clear SpellRare  
highlight SpellRare term=underline cterm=underline  
highlight clear SpellLocal  
highlight SpellLocal term=underline cterm=underline  
  
" ======================================================================================  
"                插入文件标题  
" ======================================================================================  
"新建.c,.h,.sh,.java文件，自动插入文件头   
autocmd BufNewFile *.cpp,*.[ch],*.sh,*.rb,*.java,*.py exec ":call SetTitle()"   
""定义函数SetTitle，自动插入文件头   
func! SetTitle()   
    "如果文件类型为.sh文件   
    if &filetype == 'sh'   
        call setline(1,"\#!/bin/bash")   
        call append(line("."), "")   
    elseif &filetype == 'python'  
        call setline(1, "#!/usr/bin/env python")  
        call append(line("."), "# -*- coding=UTF-8 -*-")  
        call append(line(".")+1, "#*************************************************************************")   
        call append(line(".")+2, "#   File Name: ".expand("%"))   
        call append(line(".")+3, "#   Author:JiangLin ")   
        call append(line(".")+4, "#   Mail:xiyang0807@163.com ")   
        call append(line(".")+5, "#   Created Time: ".strftime("%c"))   
        call append(line(".")+6, "#*************************************************************************")  
        call append(line(".")+7, "")   
  
    elseif &filetype == 'ruby'  
        call setline(1,"#!/usr/bin/env ruby")  
        call append(line("."),"# encoding: utf-8")  
        call append(line(".")+1, "")  
    endif  
    if expand("%:e") == 'cpp'  
        call setline(1, "/**************************************************************************")   
        call append(line("."), "   File Name: ".expand("%"))   
        call append(line(".")+1, "   Author:JiangLin ")   
        call append(line(".")+2, "   Mail:xiyang0807@163.com ")   
        call append(line(".")+3, "   Created Time: ".strftime("%c"))   
        call append(line(".")+4, "**************************************************************************/")  
        call append(line(".")+5, "#include<iostream>")  
        call append(line(".")+6, "using namespace std;")  
        call append(line(".")+7, "")  
    endif  
    if &filetype == 'c'  
        call setline(1, "/**************************************************************************")   
        call append(line("."), "   File Name: ".expand("%"))   
        call append(line(".")+1, "   Author:JiangLin ")   
        call append(line(".")+2, "   Mail:xiyang0807@163.com ")   
        call append(line(".")+3, "   Created Time: ".strftime("%c"))   
        call append(line(".")+4, "**************************************************************************/")  
        call append(line(".")+5, "#include<stdio.h>")  
        call append(line(".")+6, "#include<string.h>")  
        call append(line(".")+7, "")  
    endif  
    if expand("%:e") == 'h'  
		call setline(1, "/**************************************************************************")   
        call append(line("."), "   File Name: ".expand("%"))   
        call append(line(".")+1, "   Author:JiangLin ")   
        call append(line(".")+2, "   Mail:xiyang0807@163.com ")   
        call append(line(".")+3, "   Created Time: ".strftime("%c"))   
        call append(line(".")+4, "**************************************************************************/")  
        call append(line(".")+5, "#ifndef _".toupper(expand("%:r"))."_H")  
        call append(line(".")+6, "#define _".toupper(expand("%:r"))."_H")  
        call append(line(".")+7, "#endif")  
    endif  
    "新建文件后，自动定位到文件末尾  
endfunc   
autocmd BufNewFile * normal G  
  
" -----------------------------------------------------------------------------  
"  < 编译运行配置  
" -----------------------------------------------------------------------------  
  
let s:LastShellReturn_C = 0  
let s:LastShellReturn_L = 0  
let s:ShowWarning = 1  
let s:Obj_Extension = '.o'  
let s:Exe_Extension = '.exe'  
let s:Sou_Error = 0  
let s:Python_Extension = '.py'  
   
let s:windows_CFlags = 'gcc\ -fexec-charset=gbk\ -Wall\ -g\ -O0\ -c\ %\ -o\ %<.o'  
let s:linux_CFlags = 'gcc\ -Wall\ -g\ -O0\ -c\ %\ -o\ %<.o'  
   
let s:windows_CPPFlags = 'g++\ -fexec-charset=gbk\ -Wall\ -g\ -O0\ -c\ %\ -o\ %<.o'  
let s:linux_CPPFlags = 'g++\ -Wall\ -g\ -O0\ -c\ %\ -o\ %<.o'  
   
let s:PythonFlags = 'python\ -u\ %'  
   
func! Compile()  
    exe ":ccl"  
    exe ":update"  
    let s:Sou_Error = 0  
    let s:LastShellReturn_C = 0  
    let Sou = expand("%:p")  
    let v:statusmsg = ''  
    if expand("%:e") == "c" || expand("%:e") == "cpp" || expand("%:e") == "cxx"  
        let Obj = expand("%:p:r").s:Obj_Extension  
        let Obj_Name = expand("%:p:t:r").s:Obj_Extension  
        if !filereadable(Obj) || (filereadable(Obj) && (getftime(Obj) < getftime(Sou)))  
            redraw!  
            if expand("%:e") == "c"  
                if g:iswindows  
                    exe ":setlocal makeprg=".s:windows_CFlags  
                else  
                    exe ":setlocal makeprg=".s:linux_CFlags  
                endif  
                echohl WarningMsg | echo " compiling..."  
                silent make  
            elseif expand("%:e") == "cpp" || expand("%:e") == "cxx"  
                if g:iswindows  
                    exe ":setlocal makeprg=".s:windows_CPPFlags  
                else  
                    exe ":setlocal makeprg=".s:linux_CPPFlags  
                endif  
                echohl WarningMsg | echo " compiling..."  
                silent make  
            endif  
            redraw!  
            if v:shell_error != 0  
                let s:LastShellReturn_C = v:shell_error  
            endif  
            if g:iswindows  
                if s:LastShellReturn_C != 0  
                    exe ":bo cope"  
                    echohl WarningMsg | echo " compilation failed"  
                else  
                    if s:ShowWarning  
                        exe ":bo cw"  
                    endif  
                    echohl WarningMsg | echo " compilation successful"  
                endif  
            else  
                if empty(v:statusmsg)  
                    echohl WarningMsg | echo " compilation successful"  
                else  
                    exe ":bo cope"  
                endif  
            endif  
        else  
            echohl WarningMsg | echo ""Obj_Name"is up to date"  
        endif  
    elseif expand("%:e") == "py"  
        let Python = expand("%:p:r").s:Python_Extension  
        let Python_Name = expand("%:p:t:r").s:Python_Extension  
        if  filereadable(Python) || (!filereadable(Python) && (getftime(Python) < getftime(Sou)))  
            redraw!  
            exe ":setlocal makeprg=".s:PythonFlags  
            echohl WarningMsg | echo " compiling..."  
            silent make   
            redraw!  
            if v:shell_error != 0  
                let s:LastShellReturn_C = v:shell_error  
            endif  
            if g:iswindows  
                if s:LastShellReturn_C != 0  
                    exe ":bo cope"  
                    echohl WarningMsg | echo " compilation failed"  
                else  
                    if s:ShowWarning  
                        exe ":bo cw"  
                    endif  
                    echohl WarningMsg | echo " compilation successful"  
                endif  
            else  
                if empty(v:statusmsg)  
                    echohl WarningMsg | echo " compilation successful"  
                else  
                    exe ":bo cope"  
                endif  
            endif  
        else  
            echohl WarningMsg | echo ""Python_Name"is up to date"  
        endif  
    else  
        let s:Sou_Error = 1  
        echohl WarningMsg | echo " please choose the correct source file"  
    endif  
    exe ":setlocal makeprg=make"  
endfunc  
   
func! Link()  
    call Compile()  
    if s:Sou_Error || s:LastShellReturn_C != 0  
        return  
    endif  
    if expand("%:e") == "c" || expand("%:e") == "cpp" || expand("%:e") == "cxx"  
        let s:LastShellReturn_L = 0  
        let Sou = expand("%:p")  
        let Obj = expand("%:p:r").s:Obj_Extension  
        if g:iswindows  
            let Exe = expand("%:p:r").s:Exe_Extension  
            let Exe_Name = expand("%:p:t:r").s:Exe_Extension  
        else  
            let Exe = expand("%:p:r")  
            let Exe_Name = expand("%:p:t:r")  
        endif  
        let v:statusmsg = ''  
        if filereadable(Obj) && (getftime(Obj) >= getftime(Sou))  
            redraw!  
            if !executable(Exe) || (executable(Exe) && getftime(Exe) < getftime(Obj))  
                if expand("%:e") == "c"  
                    setlocal makeprg=gcc\ -o\ %<\ %<.o  
                    echohl WarningMsg | echo " linking..."  
                    silent make  
                elseif expand("%:e") == "cpp" || expand("%:e") == "cxx"  
                    setlocal makeprg=g++\ -o\ %<\ %<.o  
                    echohl WarningMsg | echo " linking..."  
                    silent make  
                endif  
                redraw!  
                if v:shell_error != 0  
                    let s:LastShellReturn_L = v:shell_error  
                endif  
                if g:iswindows  
                    if s:LastShellReturn_L != 0  
                        exe ":bo cope"  
                        echohl WarningMsg | echo " linking failed"  
                    else  
                        if s:ShowWarning  
                            exe ":bo cw"  
                        endif  
                        echohl WarningMsg | echo " linking successful"  
                    endif  
                else  
                    if empty(v:statusmsg)  
                        echohl WarningMsg | echo " linking successful"  
                    else  
                        exe ":bo cope"  
                    endif  
                endif  
            else  
                echohl WarningMsg | echo ""Exe_Name"is up to date"  
            endif  
        endif  
        setlocal makeprg=make  
    elseif expand("%:e") == "py"  
        return  
    endif  
endfunc  
   
func! Run()  
    let s:ShowWarning = 0  
    call Link()  
    let s:ShowWarning = 1  
    if s:Sou_Error || s:LastShellReturn_C != 0 || s:LastShellReturn_L != 0  
        return  
    endif  
    let Sou = expand("%:p")  
    if expand("%:e") == "c" || expand("%:e") == "cpp" || expand("%:e") == "cxx"  
        let Obj = expand("%:p:r").s:Obj_Extension  
        if g:iswindows  
            let Exe = expand("%:p:r").s:Exe_Extension  
        else  
            let Exe = expand("%:p:r")  
        endif  
        if executable(Exe) && getftime(Exe) >= getftime(Obj) && getftime(Obj) >= getftime(Sou)  
            redraw!  
            echohl WarningMsg | echo " running..."  
            if g:iswindows  
                exe ":!%<.exe"  
            else  
                if g:isGUI  
                    exe ":!xfce4-terminal -x bash -c './%<; echo; echo 请按 Enter 键继续; read'"  
                else  
                    exe ":!clear; ./%<"  
                endif  
            endif  
            redraw!  
            echohl WarningMsg | echo " running finish"  
        endif  
    elseif expand("%:e") == "py"  
        let python = expand("%:p:r").s:Python_Extension  
        if getftime(python) >= getftime(Sou)  
            redraw!  
            echohl WarningMsg | echo " running..."  
            if g:iswindows  
                exe ":!pythton %"  
            else  
                if g:isGUI  
                    exe ":!xfce4-terminal -x bash -c 'python %; echo; echo 请按 Enter 键继续; read'"  
                else  
                    exe ":!clear; python %"  
                endif  
            endif  
            redraw!  
            echohl WarningMsg | echo " running finish"  
        endif  
    endif  
endfunc  
  
func! RunPython()  
    exe ":w"  
    exe ":!clear; python -u %"  
endfunc  
  
"代码格式优化化  
  
"定义FormartSrc()  
func! FormartSrc()  
    exec "w"  
    if &filetype == 'c'  
        exec "!astyle --style=ansi -a --suffix=none %"  
    elseif &filetype == 'cpp' || &filetype == 'hpp'  
        exec "r !astyle --style=ansi --one-line=keep-statements -a --suffix=none %> /dev/null 2>&1"  
    elseif &filetype == 'perl'  
        exec "!astyle --style=gnu --suffix=none %"  
    elseif &filetype == 'py'||&filetype == 'python'  
        exec "r !autopep8 -i --aggressive %"  
    elseif &filetype == 'java'  
        exec "!astyle --style=java --suffix=none %"  
    elseif &filetype == 'jsp'  
        exec "!astyle --style=gnu --suffix=none %"  
    elseif &filetype == 'xml'  
        exec "!astyle --style=gnu --suffix=none %"  
    else  
        exec "normal gg=G"  
        return  
    endif  
    exec "e! %"  
endfunc  
"结束定义FormartSrc  
  
   
  
"=======================================================================  
"常用快捷键设置  
"=======================================================================  
  
" 常规模式下用空格键来开关光标行所在折叠（注：zR 展开所有折叠，zM 关闭所有折叠）  
nnoremap <space> @=((foldclosed(line('.')) < 0) ? 'zc' : 'zo')<CR>  
  
" 常规模式下输入 cS 清除行尾空格  
nmap cS :%s/\s\+$//g<CR>:noh<CR>  
  
" 常规模式下输入 cM 清除行尾 ^M 符号  
nmap cM :%s/\r$//g<CR>:noh<CR>  
  
" Ctrl + K 插入模式下光标向上移动  
imap <c-k> <Up>  
   
" Ctrl + J 插入模式下光标向下移动  
imap <c-j> <Down>  
   
" Ctrl + H 插入模式下光标向左移动  
imap <c-h> <Left>  
   
" Ctrl + L 插入模式下光标向右移动  
imap <c-l> <Right>  
"设置esc键  
imap jj <Esc>  
nmap ;; <Esc>  
vmap ;; <Esc>  
  
nmap <C-Z> <Esc>u  
"map! <C-O> <C-Y>,  
map <C-A> ggVG$"+y  
"map <F12> gg=G  
vmap <leader>y "+y  
nmap <leader>p "+p  
  
" 选中状态下 Ctrl+c 复制  
"map <C-v> "*pa  
"imap <C-v> <Esc>"*pa  
imap <C-a> <Esc>^  
imap <C-e> <Esc>$  
"vmap <C-v> "+p  
"map <c-v> "+gp  
"map <c-c> "+y  
  
" 开启/关闭对齐线  
nmap <leader>il :IndentLinesToggle<CR>  
  
" 在不使用 MiniBufExplorer 插件时也可用<C-k,j,h,l>切换到上下左右的窗口中去  
noremap <c-k> <c-w>k  
noremap <c-j> <c-w>j  
noremap <c-h> <c-w>h  
noremap <c-l> <c-w>l  
  
"行首行尾  
noremap H ^  
noremap L $  
  
" 设置NerdTree  
map <F2> :NERDTreeMirror<CR>  
map <F2> :NERDTreeToggle<CR>  
  
" 增强源代码浏览，其功能就像Windows中的"Source Insight"  
nmap <F3> :SrcExplToggle<CR>                "打开/闭浏览窗口  
  
" 常规模式下输入 tb 调用插件，如果有打开 TagList 窗口则先将其关闭  
nmap tb :TlistClose<CR>:TagbarToggle<CR>  
"nmap tb :TagbarToggle<CR>  
  
" 常规模式下输入 tl 调用插件，如果有打开 Tagbar 窗口则先将其关闭  
nmap tl :TagbarClose<CR>:Tlist<CR>  
"切换buffer  
nmap b1 :b1<CR>  
nmap b2 :b2<CR>  
nmap b3 :b3<CR>  
nmap b4 :b4<CR>  
nmap b5 :b5<CR>  
nmap b6 :b6<CR>  
nmap b7 :b7<CR>  
nmap b8 :b8<CR>  
nmap b9 :b9<CR>  
"C，C++ 按F5编译运行  
map <F5> :call Run()<CR>  
map <F8> :call RunPython()<CR>  
  
"代码格式优化化  
map <F6> :call FormartSrc()<CR>  
noremap <F1> <Esc> "废弃F1键以防调出系统帮助  
map <leader>zz :call ToggleFold()<cr>     "代码折叠快捷键  
nnoremap <C-n> :call NumberToggle()<cr>   "显示/关闭相对行号  
" 去掉搜索高亮  
noremap <silent><leader>/ :nohls<CR>  
"鼠标粘贴  
noremap <silent><leader>vb :set mouse=v<CR>  
"切换背景  
noremap <leader>bg :call ToggleBG()<CR>  
"CtrlPFunky快捷键  
nnoremap <Leader>fu :CtrlPFunky<Cr>  
" narrow the list down with a word under cursor  
nnoremap <Leader>fU :execute 'CtrlPFunky ' . expand('<cword>')<Cr>  
"ctrlpwen文件模糊查找快捷键 ctrl+p  
nnoremap <silent> <D-t> :CtrlP<CR>  
nnoremap <silent> <D-r> :CtrlPMRU<CR>  
"粘贴快捷键  
set pastetoggle=<F12>  
"<C-y>,  emmet快捷键  
"<leader><leader>fa 快速移动  
"<leader>cc，注释当前选中文本，如果选中的是整行则在每行首添加 //，如果选中一行的部分内容则在选中部分前后添加分别 / 、 /；  
"<leader>cu，取消选中文本块的注释  
"  
"<Leader>be　　全屏方式打来 buffer 列表  
"<Leader>bs　　水平窗口打来 buffer 列表  
"<Leader>bv　　垂直窗口打开 buffer 列表  
```  
