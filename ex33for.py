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
"""
At the top i is 0
Numbers now: [0]
At the bottom i is 1
At the top i is 1
Numbers now: [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now: [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now: [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now: [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now: [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers: 
0
1
2
3
4
5
"""

# 去掉递增的调用结果
"""
At the top i is 0
Numbers now: [0]
At the bottom i is 0
At the top i is 1
Numbers now: [0, 1]
At the bottom i is 1
At the top i is 2
Numbers now: [0, 1, 2]
At the bottom i is 2
At the top i is 3
Numbers now: [0, 1, 2, 3]
At the bottom i is 3
At the top i is 4
Numbers now: [0, 1, 2, 3, 4]
At the bottom i is 4
At the top i is 5
Numbers now: [0, 1, 2, 3, 4, 5]
At the bottom i is 5
The numbers: 
0
1
2
3
4
5
"""