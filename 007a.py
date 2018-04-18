# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
___title__ : 007a.py
__author__ : LongLee
___date___ : 2017/3/3 17:01
__Software : PyCharm
"""


def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:
        print(int(str(x)[::-1]))
    else:
        x1 = abs(x)
        print(int('-'+str(x1)[::-1]))

reverse(self=(), x=0)