#! /urs/bin/env python
# coding=utf-8

# 转义字符

tabby_cat = "\tI'm tabbed in." # \t 水平制表符
persian_cat = "I'm split\non a line." # \n 换行
backslash_cat = "I'm \\ a \\ cat." # \\ 反斜杠

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
