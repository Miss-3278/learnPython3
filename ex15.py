#! /urs/bin/env python
# coding= utf-8

from sys import argv # 从 sys 软件包中，取出「argv命令行参数」特性来使用

script, filename = argv

txt = open(filename) # 打开一个文件，默认为'r'模式，即读取模式

print("Here's your file %r: " % filename)
print(txt.read()) # read(), 从打开的文件中读取字符串
txt.close()

print("Tpye the filename again: ")
file_again = raw_input("> ")

txt_again = open(file_again)

print(txt_again.read()) 
txt_again.close()