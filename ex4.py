#! urs/bin/env Python
# coding=utf-8

cars = 100 # 用 = 符号给数值起一个名字，用来指代这个数值；又或者叫做给变量赋值
space_in_a_car = 4.0 # 4.0 是一个浮点数
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # 给 cars - drivers 的值，赋给变量 cars_not_driven
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
agverage_passengers_per_car = passengers / cars_driven

print("There are " + str(cars) + " cars available.")
print("There are only " + str(drivers) + " drivers available.")
print("There will be " + str(cars_not_driven) + " empty cars today.")
print("We can transport " + str(carpool_capacity) + " people today.")
print("We have " + str(passengers) + " to carpool today.")
print("We need to put about " + str(agverage_passengers_per_car) + " in each car.")
