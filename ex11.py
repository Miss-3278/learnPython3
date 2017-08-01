#! /urs/bin/evn python
# coding=utf-8

# raw_input()和 input()函数的区别
# input()函数会把你输入的东西当做 python 代码进行处理，这么做会有安全问题，应该尽量避免这个函数

print("How old are you?"),  # print 后加一个逗号（ ，），这样 print 就不会输入换行符而结束一行跑到下一行去了
age = raw_input() # raw_input 读取控制台的输入与用户实现交互。
print("How tall are you?"),
height = raw_input()
print("How much do you weigh?"),
weight = raw_input()

print("So, you're %r old, %r tall and %r heavy.") % (
    age, height, weight)
    
