#! /urs/bin/env python
# coding=utf-8

# raw_input() 可以显示一个提示

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print("So, you're %r old, %r tall and %r heavy." )% (
    age, height, weight) # %r 用来调试，%s 用来显示
    