#! /urs/bin/env Python
# coding=utf-8

# Here's some new strange stuff, remember type it exactly.
# 字符串扩展到多行（狭义理解为换行）的两种方法

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # \n 为换行符，跟在字符串的后面表示换行

print("Here are the days: " + days)
print("Here are the months: " + months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")    # """...""" 三个连续引号（单引号或者双引号）表示多行注释，可以在三个引号之间放入任意多行文字

