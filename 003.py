# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
__title__ = '003.py'
__author__ = 'LongLee'
__date__ = ' 2017/3/3'
__Software : PyCharm
"""

def lengthofstring(string):
    s = []
    for i in range(len(string)):
        if string[i] in s:
            continue
        else:
            s.append(string[i])
    print(len(s))

lengthofstring('a b ')