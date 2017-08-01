#!/urs/bin/env python
# coding=utf-8

# 使用等于号=以及 return，将变量设置为“一个函数的值”

def add(a, b):
    print("ADDING %d + %d" % (a, b)) # 打印“ADDING a + b”
    return a + b # 返回 a + b 的值，将放在等号=右边的东西作为一个函数的值返回
    
def subtract(a, b):
    print("SUBTRACTING %d -%d" % (a, b))
    return a - b
    
def multiply(a, b):
    print("MULTTPLING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b
    
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)  

print("Age: %d, Hight: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: " + str(what) + " Can you do it by hand?") 

math = add(24, subtract(divide(34, 100), 1023))
print(math)
print(float(math))

# 计算后除法四舍五入成正数了 


    