#! /urs/bin/env python
# coding=utf-8

# 函数

# this one is like your scripts with argv
def print_two(*args): # 定义函数，函数名字最好能体现函数功能。*号意思是把所有参数都接受进来，然后放到名叫 argv 的列表中去
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # 函数可以直接使用括号里面的名称作为变量名称
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    
# this just takes one argument
def print_one(arg1): # 函数接收单个参数
    print("arg1: %r" % arg1)
    
# this one takes no arguments
def print_none(): # 函数不接收参数
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

"""
1. 定义函数以 def 开始
2. 函数名以字符和下划线_组成
3. 函数名紧跟着括号(
4. 函数若包含多个参数，以逗号隔开
5. 紧跟着参数的是括号和冒号):
6. 紧跟着函数定义的代码使用 4 个空格缩进
7. 函数结束的位置取消缩进
"""