#! /urs/bin/env python
# coding=utf-8

"""
sys.argv[] 是命令行参数，实现从程序外部像程序内部传递参数
sys.argv[0] 是脚本名称，代表本身文件路径，因此，参数从 1 开始
在运行脚本时用命令行将参数传递给脚本
"""

from sys import argv

script, first, second, third = argv   # 将命令行输入的参数赋值给 3 个变量, 命令行参数第[0]个变量为脚本名称

print("The script is called: " + script)
print("Your first variable is: " + first)
print("Your second variable is: " + second)
print("Your third variable is: " + third)

# 输出结果显示
"""
$ python ex13.py stuff things that
  The script is called: ex13.py
  Your first variable is: stuff
  Your second variable is: things
  Your third variable is: that
"""



