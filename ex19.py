#! /urs/bin/env python
# coding=utf-8

# 可以直接给函数传递数字、变量、数学表达式，甚至数学表达式和变量合起来用

def cheeses_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blank.\n")
    
print("We can just give the function numbers directly:")
cheeses_and_crackers(20, 30) # 给变量的参数赋值，并且调用函数

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheeses_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheeses_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheeses_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 一个物件可以用=对其冥冥，通常也可以将其作为参数传递给一个函数
