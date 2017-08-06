#! /urs/bin/env python
# coding=utf-8

# 字典 dict 及其用法。字典的内容是无序的，可以通过某一个值对应到另外一个值，叫「键值对」

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}



# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# add some more cities 
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: " + cities['NY']) # New York
print("OR State has: " + cities['OR']) # Portland

# print some states
print('-' * 10)
print("Michigan's abbreviation is: " + states['Michigan']) # MI
print("Florida's abbreviation is: " + states['Florida']) # FL

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: " + cities[states['Michigan']]) # Detriot
print("Florida has: " + cities[states['Florida']]) # Jacksonville

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items(): # dict.items(),返回字典中包含键和值得元组。
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():    
    print("%s has the city %s" % (abbrev, city))
    
# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is avvreviated %s and has city %s." % (state, abbrev, cities[abbrev]))
    
print('-' * 10)
# safely get a abbreviation by state that might not be there 
state = states.get("Texas", None) 
# dict.get()方法有两个参数，一是要取得值的键，二是如果该键值不存在，返回的备用值。如果字典中没有该键值，get 方法不会产生错误消息。

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get("TX", 'Dose not Exist') # 字典中添加'TX' 键，其对应值为' Dose not exist'
print("The city for the state 'TX' is: %s" % city)
