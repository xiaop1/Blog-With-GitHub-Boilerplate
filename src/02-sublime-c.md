---
layout: post
title: Win下搭建Sublime的C语言环境
slug: sublime
date: 2020-01-08 22:12
status: publish
author: 小皮
categories: 
  - 默认分类
tags: 
  - Win
  - Sublime
excerpt: Sublime Text is a sophisticated text editor for code, markup and prose.
---

## Sublime安装

[Sublime](https://www.sublimetext.com/)是一款用于代码、标记和散文的精致文本编辑器。Sublime的安装可以在官网或者百度中搜索安装包，安装很简单（无需安装到C盘）。

Sublime不仅可以用来当作文本编辑器，同时可以通过安装C、Python等语言的环境来当作简单的编译器来使用（不支持代码调试）。而且Sublime可以安装数以万计的插件，来提高工作效率。

![介绍](./images/sublime-introduce.gif)

## TDM-GCC安装

MinGW是Windows的Minimallist GNU的缩写，是用于本机Microsoft Windows应用程序的简约开发环境。

网上常见的教程为使用MinGW环境，然而MinGW更新缓慢而且安装后可能出现问题，这里推荐使用[TDM-GCC官网下载](http://tdm-gcc.tdragon.net/download)。（无需安装到C盘）

安装后最重要的一步为配置系统变量，按照你所安装路径配置系统变量，配置过程如下图所示。配置后，在开始中输入CMD，在命令提示窗口执行`gcc --help`，如果能看到编译环境的帮助页面说明配置成功。

![配置系统变量](./images/mingw-env.png)

## Sublime配置

安装好C语言环境后，还有最后一步就是配置Build System，Sublime需要运行Build System才能执行代码。

在工具栏找到`Tools->Build System->New Build System`，将下面的代码复制到你新建的Build System中，保存为`c.sublime-build`。

```c
{
"cmd": ["gcc","-Wall", "${file}", "-o", "${file_path}/${file_base_name}"],
"file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
"working_dir": "${file_path}",
"selector": "source.c, source.c++",
"encoding":"cp936",
"variants":
[
{
"name": "Run",
"cmd": ["cmd", "/c", "gcc", "-Wall","${file}", "-o", "${file_path}/${file_base_name}", "&&", "cmd", "/c", "${file_path}/${file_base_name}"]
},
{
"name": "RunInCommand",
"cmd": ["cmd", "/c", "gcc", "-Wall","${file}", "-o", "${file_path}/${file_base_name}", "&&", "start", "cmd", "/c", "${file_path}/${file_base_name} & echo.&pause"]
},
{
"name": "RunInShell",
"shell_cmd": " start cmd /c \"\"${file_path}/${file_base_name}\"&pause\" "
}
]
}
```

新建一个C文件，然后保存后输入简单的代码，按CTRL+Shift+b，就会显示你将要用什么来编译它，如果你是按照我上面的代码配置的话，你将看到C-Run、C-RunInCommand、C-RunInShell其中你点C-Run，你就可向下图一样显示了。下次运行代码，你就可以按CTRL+b就可以运行了，这个是表示接着用上次编译方式进行。

![成功运行](./images/sublime-c-run.jpg)

## 总结

本文通过说明在Win下如何搭建Sublime的C语言环境，介绍了一种轻量级编译代码的方式，通过这种方式不仅可以编译C语言，同理也可以编译Python等语言。同时借助其强大的插件，可以几乎替代代码编译器。