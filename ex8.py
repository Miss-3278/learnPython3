#! /urs/bin/env Python
# coding=utf-8

formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

# 输出"But it didn't sing."时，字符串中包含了单引号，所以在输出的时候显示为双引号。
# 字符串中包含有单引号的用双引号括起来用来区分；字符串中没有单引号在输出时显示单引号。