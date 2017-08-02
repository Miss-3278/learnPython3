#! /urs/bin/env python
# coding=utf-8

# 字符串的切片、排序、移除

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # split() 通过制定分隔符对字符串进行切片
    return words
    
def sort_words(words):
    """Sorts the words."""
    return sorted(words) # sort() 函数，对列表进行排序，并且生成一个新的列表
    
def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0) # pop() 方法，用于移除列表中的一个元素（默认最后一个元素，并返回该元素的值
    print(word) 
    
def print_last_word(words):
    """print the last word after popping it off"""
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) # 变量 words 对 sentence 变量定义的字符串切片
    return sort_words(words) # 返回 sort_words 函数，对字符串的切片进行排序
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words the prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
# 在终端检查错误，在 IDLE 运行，结果显示
"""
>>> import os
>>> os.chdir("/users/lixun/Python/learnPython3")
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.sort_words(sentence)
>>> words
[' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', 'A', 'a', 'c', 'd', 'e', 
'e', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'l', 'l', 'm', 'n', 'o', 
'o', 'o', 'o', 'o', 'o', 's', 's', 't', 't', 't', 't', 'w', 'w']
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who

"""
