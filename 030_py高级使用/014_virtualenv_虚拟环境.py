#!/usr/bin/env python
# coding: utf-8

""
"""
 -------------------------- virtualenv 虚拟环境 ----------------------------
1 : virtualenv 是一个工具，它能提供我们一个独立(隔离)的Python环境 ;
2 : virtualenv 针对每一个应用程序创建独立的Python环境 , 而不是在全局安装所依赖的模块 ;

3 : 安装 pip install virtualenv
4 : virtualenv myproject           (在myproject文件夹创建一个隔离的virtualenv环境)
5 : source myproject/bin/activate  (激活这个隔离的虚拟环境) 
6 : deactivate                     (退出虚拟环境)

7 : 如果你想让你的virtualenv使用系统全局模块，请使用--system-site-packages参数创建你的virtualenv，例如: 
    virtualenv --system-site-packages mycoolproject
8 : 你可以使用smartcd来帮助你管理你的环境，当你切换目录时，它可以帮助你激活（activate）和退出（deactivate）你的virtualenv
"""
