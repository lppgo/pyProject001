#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pretty_errors

pretty_errors.configure(
    separator_character='*',
    filename_display=pretty_errors.FILENAME_EXTENDED,
    line_number_first=True,
    display_link=True,
    lines_before=5,
    lines_after=2,
    line_color=pretty_errors.RED + '> ' + pretty_errors.default_config.line_color,
    code_color='  ' + pretty_errors.default_config.line_color,
)


def foo():
    print(4 / 2)
    print(4 // 2)
    print(4 / 0)


foo()


"""  ---------------------- pretty_errors  是python 错误美化的library ----------------------- """
# 1 : 安装
# python - m pip install pretty_errors

# 2 : 单个项目引入
# import pretty_errors

# 3 : 全局生效，其他项目也可以生效
# python -m pretty_errors
