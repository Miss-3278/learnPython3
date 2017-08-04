#! /urs/bin/env python
# coding=utf-8

# if 条件语句，伪代码创建一个所谓的“分支”：如果布尔表达式为真，就运行接下来的代码，否则就跳过这一段

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
    
if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")
    
if people > dogs:
    print("The world is dry!")
    
dogs += 5 # +=叫做递增运算符

if people >= dogs:
    print("People are greater than or equal to dogs.")
    
if people <= dogs:
    print("People are less than or equal to dogs.")
    
if people == dogs:
    print("People are dogs.")