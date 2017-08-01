#! /urs/bin/env python
# coding=utf-8

print("I will now count my chickens:") # 打印这句话

print("Hens " + str(25 + 30 / 6)) # 打印 Hens, 并把数学公式计算出来的数值转换为字符串，一起打印
print("Roosters " + str(100 - 25 * 3 % 4)) 
# 如果用 print（“Roosters”， 100 - 25 * 3 % 4），打印出来的是一个元组（Roosters， 97）

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) 
# % 表示求余数，“X 除以 Y 还剩余 J”，% 运算的结果就是 J 这部分。例如“100 除以 16 还剩余 4”，J = 4

print("Is it true that 3 + 2 < 5 -7?")

print(3 + 2 < 5 - 7) # 比较逻辑关系“小于”，返回 True or False

print("What is 3 + 2? " + str(3 + 2))
print("What is 5 - 7? " + str(5 - 7))

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater? " + str(5 > -2))
print("Is it greater or equal? " + str(5 >= 2))
print("Is it less or equal? " + str(5 <= 2))