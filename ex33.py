#! /urs/bin/env python
# coding=utf-8

# while 循环，一直执行下面的代码块，知道它对应的布尔表达式为 False 才会停下来。停不下来时用 Ctrl+C

i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: " + str(numbers))
    print("At the bottom i is %d" % i)
    
print("The numbers: ")

for num in numbers:
    print(num)