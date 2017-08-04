#! /urs/bin/env python
# coding=utf-8

# for 循环语句 & 列表

the_count = [1, 2, 3, 4, 5] # 列表
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number) # 打印1，2，3，4，5

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit) # 打印四种水果
    
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)
    
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6): # range()函数，创建一个整数列表，用于 for 函数中。可以设置三个参数开始，结束和补偿。结束不包含最后一个数，即含首不含尾
    print("Adding %d to the list." % i)
    # append if a function that lists understand
    elements.append(i) # 在列表末尾添加元素
    
# now we can print them out too
for i in elements: # elements 的值为0~5
    print("Element was: %d" % i)