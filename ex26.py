#!/urs/bin/env python
# coding=utf-8

import ex25

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # 对字符串进行切片
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) # sort 这里是将……排序的意思

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # 移除列表中第一个元素
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # 移除最后一个元素
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) # 对变量 sentence 进行切片
    return sort_words(words) # 返回切片的排序

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) # 切片
    print_first_word(words) # 移除第一个元素
    print_last_word(words)  # 移除最后一个元素

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) # 切片，排序
    print_first_word(words) # 移除第一个元素
    print_last_word(words)  # 移除最后一个元素


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words) # All
print_last_word(words)  # weight
print_first_word(sorted_words) # All
print_last_word(sorted_words)  # who, 按照切片后排序的顺序来的
sorted_words = ex25.sort_sentence(sentence) # 对 sentence 变量进行切片，返回切边的排序
print(sorted_words)

print_first_and_last(sentence) # All

print_first_and_last_sorted(sentence) # weight


"""
1. 16行 poop --> pop
2. 21行 最后加括号 ）
3. 14行 函数最后加冒号 ：
4. 70行 == --> = ; start-point --> start_point
5. 73行 jeans --> beans
6. 78行 start_pont --> start_point; 最后加上两个括号 ））
7. 88行 去掉第一个.
8. 91行 prin --> print
9. 93行 irst --> first
10. 95行 a --> and; senence --> sentence
11. 64行 \ --> / , 表示运算中的除法
12. 在程序首行（第4行）写 import ex25,因为后面要用到 ex25.py
13. 18、19、43、44、56、58、61、73、74、78、79、92行的 print 函数改写成 Python3 语法规则，为 print（）

"""