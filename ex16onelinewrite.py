#! /urs/bin/env python
# coding=utf-8

from sys import argv

scriot, filename = argv

print("We're going to erease %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

raw_input("?")

print("Opening the file...")
target = open(filename, 'w') # 参数 w，表示打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

print("Truncating the file. Goodbye!")
target.truncate() 

"""
File.truncate（）方法用于截断文件。不指定参数就是清空文件。
如果制定了可选参数 size，则表示截断文件为 size 这个字符。
如果没有指定 size，则从当前位置其截断；阶段后 size 后面的所有字符被删除。
"""

print("Now I'm going to ask you for three lines.")

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print("I'm going to write these to the file.")

line = line1 + "\n" + line2 + "\n" + line3

target.write(line)

print("And finally, we close it.")
target.close() # 关闭文件，关闭后不能再读写文件
