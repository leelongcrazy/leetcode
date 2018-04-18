# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
___title__ : 006a.py
__author__ : LongLee
___date___ : 2017/3/3 18:21
__Software : PyCharm
"""

def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s

    L = [''] * numRows
    index, step = 0, 1

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    print(''.join(L))

convert(self=(),s='leelongcrazy',numRows=3)