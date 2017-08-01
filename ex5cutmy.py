#! /urs/bin/env Python
# coding=utf-8

# 变量名要以字母开头，数字不是有效的变量名称
name = "Zed A. Shaw" 
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = "Blue"
teeth = "white"
hair = "Brown"

print("Let's talk about %s." % name) # 把 my_name 变量带入到字符串当中
print("He's %d inches tall." % height) # 把 my_height 变量带入到字符串中
print("He's %d pounds heavy." % weight) # 把 My_weight 变量带入到字符串中
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair)) # 把 my_eyes, my_hair 变量带入到字符串中
print("His teeth are usually %s depending on the coffee." % teeth) # 把 my_teeth 变量带入到字符串中

# this line is tricky, try to get it exactly right

print("If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight))