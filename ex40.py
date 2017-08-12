#! /urs/bin/env python
# coding=utf-8

# 从某个东西里获取东西的三个相似但原理不同的方法：字典 dict，模块 module，类 class。

class Song(object):  # 创建一个类，名字叫做 Song，它是 object 的一种
    
    def __init__(self, lyrics): # 初始化函数，将初始化的属性放到这个函数里，self 这个参数是必须的
    # 类 Song 有一个 __init__,接收 self 和 lyrics 作为参数
        self.lyrics = lyrics  # 为初始参数设置默认值，用点（.）的方式，给参数赋值
        
    def sing_me_a_song(self): # 类 Song 有一个函数名为 sing_me_a_song, 它接收 self 参数
        for line in self.lyrics: 
            print(line)
            
    def sing_a_song(self):
       for lines in self.lyrics:
           print(lines)
        
happy_baby = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]) # 类 Song 实例化，就是将具体的歌词传给 Song 类
                
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"]) # 实例化
                        
yuanchen = Song(["多谢你如此精彩耀眼",
                 "做我平淡岁月里星辰"]) # 将 yuanchen 设为类 Song 的一个实例
                 
jiewo = Song(["借我不惧碾压的鲜活",
              "借我生命与猛撞不问明天",
              "借我一束光照亮黯淡",
              "借我笑颜灿烂如春天"]) # 实例化
                    
happy_baby.sing_me_a_song() 

bulls_on_parade.sing_me_a_song()

yuanchen.sing_me_a_song() # 从 yuanchen 中找到 sing_me_a_song 属性，使用 self 参数调用它

jiewo.sing_a_song()