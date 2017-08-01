#! /urs/bin/env Python
# coding=utf-8

my_name = "Zed A. Shaw" # 变量名要以字母开头，数字不是有效的变量名称
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = "Blue"
my_teeth = "white"
my_hair = "Brown"

print("Let's talk about %s." % my_name) # 把 my_name 变量带入到字符串当中
print("He's %d inches tall." % my_height) # 把 my_height 变量带入到字符串中
print("He's %d pounds heavy." % my_weight) # 把 My_weight 变量带入到字符串中
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair)) # 把 my_eyes, my_hair 变量带入到字符串中
print("His teeth are usually %s depending on the coffee." % my_teeth) # 把 my_teeth 变量带入到字符串中

# this line is tricky, try to get it exactly right

print("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))