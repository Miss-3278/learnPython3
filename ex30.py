#! /urs/bin/env python
# coding=utf-8

# elif & else 条件语句

people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, Let's just take the buses.")
else:
    print("Fine, Let's stay home then.")
    