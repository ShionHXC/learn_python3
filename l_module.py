#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'hxc'
# 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
# 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

import sys
def test():
    args = sys.argv
    print(args)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()