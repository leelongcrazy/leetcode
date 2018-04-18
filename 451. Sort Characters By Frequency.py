#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
"""
    Time    : 2018/4/12 22:49
    Author  : LeeLong
    File    : 451. Sort Characters By Frequency.py
    Software: PyCharm
    Description:Given a string, sort it in decreasing order based on the frequency of characters.
"""


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        d = {}
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        l = []
        for i in d.values():
            l.append(i)
        l.sort(reverse=True)
        ss = []
        for i in l:
            d.
        print(l)


r = Solution()
r.frequencySort('aabbb')
