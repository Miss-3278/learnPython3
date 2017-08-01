#! /urs/bin/env python
# coding=utf-8

# 函数和文件在一起协作
# 调用命令写成 python3 ex20.py input_file,要不然 line18 会报错

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0) # 设置当前文件的位置，seek 处理对象是字节，seek(0)是到 0 byte，也就是第一个字节的位置
    
def print_a_line(line_count, f):
    print(str(line_count) + " " + f.readline(), end='') 
    
"""
readline()从文件中读取整行，包括\n字符。
文件 f 会记录每次调用 readline() 后的读取位置，这样就可以在下次被调用时读取接下来的一行了。
"""
 
"""
 readline() 函数返回的内容中包含文件本来就有的\n(换行）,
 而 print 在打印时又会添加一个\n.
 这样一来，打印就多出一个空行。解决方法是：
 1. python2 环境，print 语句结尾加一个逗号（ ，）
 2. python3 环境，print 语句结尾加上 , end=''。这样会将\n（换行）替换为空值。
"""   
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file) # 先打开input_file,然后调用函数读取input_file 并打印

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # 打开input_file，然后到文件的开始

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) # 第一行，读取input_file第一行并打印

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
