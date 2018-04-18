# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
___title__ : 007.py
__author__ : LongLee
___date___ : 2017/3/3 16:27
__Software : PyCharm
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            if int(str(x)[::-1]) < 2**31-1:
                print(int(str(x)[::-1]))
            else:
                print(0)
        else:
            x1 = abs(x)
            if int('-' + str(x1)[::-1]) > -2**31+1:
                print(int('-' + str(x1)[::-1]))
            else:
                print(0)

    reverse(self=(), x=-123456789)