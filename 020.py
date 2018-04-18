# /usr/bin/env python
# --*-- coding:utf-8 --*--
"""
___title__ : 020.py
__author__ : LongLee
___date___ : 2017/3/18 13:26
__Software : PyCharm
"""


def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    con = []
    dic = {')':'(', ']':'[', '}':'{'}
    if len(s) == 0:
        return True
    elif len(s) != 2 and len(s)%2 == 1:
        return False
    else:
        for em in s:
            if em in dic.values():
                con.append(em)
            elif em in dic.keys():
                if con == [] or dic[em] != con.pop():
                    return False
            else:
                return False
        return con == []
