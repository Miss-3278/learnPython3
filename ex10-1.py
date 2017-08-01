#! /urs/bin/env python
# coding=utf-8

# 不停地换行打印五种符号，按 command+D 结束
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i) # \r 回车符