#! /urs/bin/env python
# coding=utf-8

# 从某个东西里获取东西的三个相似但原理不同的方法：字典 dict，模块 module，类 class。

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
    def sing_a_song(self):
       for lines in self.lyrics:
           print(lines)
        
happy_baby = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
yuanchen = Song(["多谢你如此精彩耀眼",
                 "做我平淡岁月里星辰"])
                 
jiewo = Song(["借我不惧碾压的鲜活",
              "借我生命与猛撞不问明天",
              "借我一束光照亮黯淡",
              "借我笑颜灿烂如春天"])
                    
happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

yuanchen.sing_me_a_song()

jiewo.sing_a_song()