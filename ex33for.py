#! /urs/bin/env python
# coding=utf-8

# 将 while 循环换成 for 循环，这时不需要中间的递增操作

i = 0
numbers = []

for i in range(0, 6):
    print("At the top i is %d" % i)
    numbers.append(i)
    
    
    print("Numbers now: " + str(numbers))
    print("At the bottom i is %d" % i)
    
print("The numbers: ")

for num in numbers:
    print(num)
 
# 不去掉递增的调用结果
   

