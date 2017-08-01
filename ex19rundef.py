#! /urs/bin/env python
# coding=utf-8

def pen_and_pencil(count1, count2):
    print("Hi, I have %s pencils" % count1)
    print('Oh, I have %s pens' % count2)
    print("That's good")   

pen_and_pencil(4, 10)


pen_and_pencil(4 + 5, 10 - 8)


pens = 6
pencils = 9
pen_and_pencil(pens, pencils)

pen_and_pencil(pens / 2, pencils + 3)

