#! /urs/bin/env Python
# coding=utf-8

# %r 用来做调试最好，因为它会显示变量的原始数据。也就是说，%r 给你的是变量的“程序员原始版本”，又被称作是“原始表示”
# %s 和其它的符号用来向用户显示变量的，也就是 %s 打印的是作为用户应该看到的东西

x = "There are %d types of people." % 10 # 给变量 x 赋值给一个字符串，并将 10 带入字符串当中
binary = "binary" # 变量 binary 赋值给字符串 "binary"
do_not = "don't"  # 变量 do_not 赋值给字符串 "don't"
y = "Thoes who know %s and those who %s." % (binary, do_not) # 变量 y 赋值给字符串，并将变量 binary 和 do_not 带入字符串

print(x) # 打印变量 x
print(y) # 打印变量 y

print("I said: %r." % x) # 打印字符串，并将变量 x 带入字符串。 这个地方把 %r 改成 %s，打印出的效果一样，但原理不一样。
print("I also said: '%s'." % y) # 打印字符串，并将变量 y 带入字符串

hilarious = False # 给变量 hilarious 赋值给布尔值
joke_evaluation = "Isn't that joke so funny?! %r" # 变量 joke_evaluation 赋值字符串，字符串中包含格式化字符

print(joke_evaluation % hilarious) # 打印 joke_evaluation 变量，并将变量 hilarious 带入字符串

w = "This is the left side of ..." # 变量 w 赋值给字符串
e = "a string with a right side. " # 变量 e 赋值给字符串

print(w + e) # 连接 w 和 e，并打印。+ 号连接两个变量
