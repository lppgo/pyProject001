#!/usr/bin/python

""" 包 """

# 包是管理Python模块命名空间的形式，采用'点模块名称'
# A.B  表示A包中的B模块
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包 ;
# 最简单的情况，放一个空的: file: __init__.py就可以了;
# 当然这个 __init__.py 文件中也可以包含一些初始化代码或者为 __all__ 变量赋值 ;

""" 
用户可以每次只导入一个包里面的特定模块,比如: 
    import sounds.effects.echo       
    from sounds.effects import echo  
    from sound.effects.echo import echofilter 


注意当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量;
如果使用形如 import item.subitem.subsubitem 这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字

 """
