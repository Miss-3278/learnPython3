#! /urs/bin/env python
# coding=utf-8

print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

# \t水平制表符；\n换行符；\转义字符；\\斜杠

pome = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------------")
print(pome)
print("----------------")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# 两种不同的方法：一是直接调用函数，二是调用函数中的变量

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))
# jelly_beans 和 beans 是两个变量。这是函数的工作原理，函数内部的变量都是临时的，当函数返回以后，返回值可以被赋予另外一个变量。
# beans 就是创建的新变量，用来存放函数的返回值。

start_point = start_point / 10

print("We can also do that this way: ")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))